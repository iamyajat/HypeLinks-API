import tensorflow as tf
import numpy as np
from tqdm import tqdm
from transformers import DistilBertTokenizer, DistilBertConfig, TFDistilBertModel
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI(
    title="Smart Bookmark",
    version="1.0",
    description="Classifies the sites into various different categories",
)

maxlen = 100
vocab_size = 15000
embed_size = 64
distil_bert = "distilbert-base-uncased"


save_directory = "./models/tokenizer/"

tokenizer = DistilBertTokenizer.from_pretrained(save_directory)


def tokenize(sentences, tokenizer):
    input_ids, input_masks = [], []
    for sentence in tqdm(sentences):
        inputs = tokenizer.encode_plus(
            sentence,
            add_special_tokens=True,
            max_length=maxlen,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_token_type_ids=True,
        )
        input_ids.append(inputs["input_ids"])
        input_masks.append(inputs["attention_mask"])

    return np.asarray(input_ids, dtype="int32"), np.asarray(input_masks, dtype="int32")


def pred_model():
    config = DistilBertConfig(dropout=0.4, attention_dropout=0.4)
    config.output_hidden_states = False
    transformer_model = TFDistilBertModel.from_pretrained(distil_bert, config=config)

    input_ids_in = tf.keras.layers.Input(
        shape=(maxlen,), name="input_token", dtype="int32"
    )
    input_masks_in = tf.keras.layers.Input(
        shape=(maxlen,), name="masked_token", dtype="int32"
    )

    embedding_layer = transformer_model.distilbert([input_ids_in, input_masks_in])[0]
    X = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True))(
        embedding_layer
    )
    X = tf.keras.layers.GlobalMaxPool1D()(X)
    X = tf.keras.layers.Dense(64, activation="relu")(X)
    X = tf.keras.layers.Dropout(0.4)(X)
    X = tf.keras.layers.Dense(10, activation="softmax")(X)
    model = tf.keras.Model(inputs=[input_ids_in, input_masks_in], outputs=X)

    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"],
    )

    model.load_weights("models/weights/weights3.h5")
    is_model = True
    return model


model = pred_model()


def get_title(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")
    test = []
    for title in soup.find_all("title"):
        test.append(str(title.get_text()))
    return test[0:1]


labels = {
    0: "Sports",
    1: "News",
    2: "Fitness & Wellbeing",
    3: "Food and Recipes",
    4: "NSFW",
    5: "Politics",
    6: "Entertainment",
    7: "Business",
    8: "Blogs",
    9: "Science & Technology",
}


@app.get("/")
async def index():
    return {"message": "Smart Bookmark is online"}


@app.get("/list")
async def index():
    return [v for k, v in labels.items()]


class Input(BaseModel):
    data: str


@app.post("/classify")
async def get_item(input: Input):
    try:
        url = input.data
        print(url)
        title = get_title(url)
        print(title)
        test_seq = tokenize(title, tokenizer)
        test_preds = labels[np.argmax(model.predict(test_seq)[0])]
        print(test_preds)
        return {"title": title[0], "category": test_preds}
    except:
        return {"message": "Error"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)