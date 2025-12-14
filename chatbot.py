import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json") as file:
    data = json.load(file)

corpus = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        corpus.append(pattern)
        labels.append(intent["tag"])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

model = LogisticRegression()
model.fit(X, labels)

def chatbot_response(text):
    text = text.lower()
    vector = vectorizer.transform([text])
    tag = model.predict(vector)[0]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
