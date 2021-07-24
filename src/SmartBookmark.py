from transformers import MobileBertTokenizer, MobileBertConfig, TFMobileBertModel
import tensorflow as tf
import numpy as np
import numpy as np
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

labels = {
    0: "Politics",
    1: "Science & Technology",
    2: "Blogs",
    3: "Business",
    4: "Food and Recipes",
    5: "Fitness & Wellbeing",
    6: "News",
    7: "Sports",
    8: "NSFW",
    9: "Entertainment",
}

maxlen = 100
vocab_size = 15000
embed_size = 64
mobile_bert = "google/mobilebert-uncased"

token_directory = "./assets/tokenizer/"
weights_directory = "./assets/weights/weights.h5"

tokenizer = MobileBertTokenizer.from_pretrained(token_directory)


def tokenize(sentences, tokenizer):
    input_ids, input_masks = [], []
    for sentence in tqdm(sentences):
        inputs = tokenizer.encode_plus(
            sentence,
            add_special_tokens=True,
            max_length=maxlen,
            padding="max_length",
            return_attention_mask=True,
            return_token_type_ids=True,
        )
        input_ids.append(inputs["input_ids"])
        input_masks.append(inputs["attention_mask"])

    return np.asarray(input_ids, dtype="int32"), np.asarray(input_masks, dtype="int32")


def pred_model():
    config = MobileBertConfig(dropout=0.4, attention_dropout=0.4)
    config.output_hidden_states = False
    transformer_model = TFMobileBertModel.from_pretrained(mobile_bert, config=config)

    input_ids_in = tf.keras.layers.Input(
        shape=(maxlen,), name="input_token", dtype="int32"
    )
    input_masks_in = tf.keras.layers.Input(
        shape=(maxlen,), name="masked_token", dtype="int32"
    )

    embedding_layer = transformer_model.mobilebert([input_ids_in, input_masks_in])[0]
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

    model.load_weights(weights_directory)
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


def evaluate(url):
    print(url)
    title = get_title(url)
    print(title)
    test_seq = tokenize(title, tokenizer)
    test_preds = labels[np.argmax(model.predict(test_seq)[0])]
    print(test_preds)
    return title, test_preds
