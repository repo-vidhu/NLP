import pandas as pd
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

from datasets import load_dataset
dataset = load_dataset('sdiazlor/text-classification-news-topics', 'generate_text_classification_data_0')
df = pd.DataFrame(dataset['train'])

print(df.columns)
def preprocess_text(text):
	if not isinstance(text, str):  # Check if text is None or not a string
		return ""
	text = text.lower()
	text = re.sub(f"[{string.punctuation}]", "", text)
	text = re.sub("\d+", "", text)
	return text

df["clean_text"] = df["input_text"].apply(preprocess_text)


vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)


X = vectorizer.fit_transform(df["clean_text"])
print(df['clean_text'][3:10])

df["label"] = df["label"].fillna("unknown")
y = df["label"].astype(str)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print(classification_report(y_test, y_pred))


def classify_text(text):
    processed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)[0]
    return prediction

# Example classification
sample_text = input("Give input :")
# "The recent breakthrough in quantum computing has led to the development of a new algorithm that can efficiently solve complex optimization problems, potentially revolutionizing fields such as logistics and finance. This achievement was made possible by the creation of a novel quantum circuit that can be scaled up to larger systems, paving the way for the widespread adoption of quantum computing in various industries."
predicted_label = classify_text(sample_text)
print(f"Predicted category: {predicted_label}")
