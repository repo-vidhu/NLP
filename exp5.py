from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Sample corpus
corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "This is not the first document!"
]

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer on the corpus and transform the text into a bag of words
X = vectorizer.fit_transform(corpus)

# Convert the result to an array
X_array = X.toarray()

# Get the feature names (words in the vocabulary)
feature_names = vectorizer.get_feature_names_out()

# Create a DataFrame with the vocabulary as column headers
df = pd.DataFrame(X_array, columns=feature_names)

# Print the results
print("Vocabulary (Feature Names):")
print(feature_names)

print("\nBag of Words Matrix:")
print(df)

# If you want to see the mapping of words to indices
#print("\nWord to Index Mapping:")
#print(vectorizer.vocabulary_)

# Compute cosine similarity between the documents
cosine_sim = cosine_similarity(X_array)

# Print the cosine similarity matrix
print("\nCosine Similarity Matrix:")
print(cosine_sim)

