import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tqdm import tqdm
from transformers import AutoTokenizer
from transformers import DistilBertTokenizer, DistilBertConfig, TFDistilBertModel
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import (
    Embedding,
    LSTM,
    Conv2D,
    Conv1D,
    MaxPooling1D,
    Dense,
    Dropout,
    GlobalMaxPooling1D,
    Input,
    Bidirectional,
    concatenate,
    Flatten,
    GlobalAveragePooling1D,
)
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.utils import plot_model
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Initiate app instance
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

# data = pd.read_csv("./models/smartbookmark.csv")

# data = data.dropna().reset_index(drop=True)

# data["category"] = data["category"].astype("category")

# cat = list(set(data["category"].unique()))

# category = {cat[i]: i for i in range(len(cat))}
# data["category"] = data["category"].replace(category)

# text = np.array([str(t) for t in data['title'].values])
# labels = data['category'].values

# X_train, x_test, y_train, y_test = train_test_split(
#     text, labels, random_state=1, test_size=0.15
# )

tokenizer = DistilBertTokenizer.from_pretrained(
    save_directory,
    #     distil_bert,
    #     do_lower_case=True,
    #     add_special_tokens=True,
    #     max_length=maxlen,
    #     pad_to_max_length=True,
)
# import pickle
# with open(save_directory, 'rb') as handle:
#     tokenizer = pickle.load(handle)


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


# #
# # Tokenize desc and title train data
# X_train = tokenize(X_train, tokenizer)
# x_test = tokenize(x_test, tokenizer)


config = DistilBertConfig(dropout=0.4, attention_dropout=0.4)
config.output_hidden_states = False
transformer_model = TFDistilBertModel.from_pretrained(distil_bert, config=config)

input_ids_in = tf.keras.layers.Input(shape=(maxlen,), name="input_token", dtype="int32")
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

# for layer in model.layers[:3]:
#     layer.trainable = False

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer=Adam(learning_rate=0.001),
    metrics=["accuracy"],
)

# model = tf.keras.Model()
model.load_weights("models/weights/weights3.h5")

# model = tf.keras.models.load_model("models/weights.h5")


def get_title(url):
    # making requests instance
    reqs = requests.get(url)

    # using the BeaitifulSoup module
    soup = BeautifulSoup(reqs.text, "html.parser")

    # displaying the title
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
    return "Invalid endpoint, use /get-rating/{url}\n or /rate"


class Input(BaseModel):
    data: str


@app.post("/rate")
async def get_item(input: Input):
    url = input.data
    print(url)
    title = get_title(url)
    print(title)
    test_seq = tokenize(title, tokenizer)
    # print(test_seq)
    test_preds = labels[np.argmax(model.predict(test_seq)[0])]
    print(test_preds)
    return {"title": title[0], "category": test_preds}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)