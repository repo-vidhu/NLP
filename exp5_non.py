import math
import pandas as pd
from collections import Counter

# Sample corpus
corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "This is not the first document!"
]

# Function to tokenize text into words and normalize (lowercase and remove punctuation)
def tokenize(text):
    return text.lower().split()

# Tokenize the corpus
tokenized_corpus = [tokenize(doc) for doc in corpus]

# Build the vocabulary (unique set of all words across the corpus)
vocabulary = sorted(set(word for doc in tokenized_corpus for word in doc))

# Create a bag-of-words matrix
def create_bow_matrix(corpus, vocabulary):
    matrix = []
    for doc in corpus:
        word_count = Counter(doc)
        row = [word_count.get(word, 0) for word in vocabulary]
        matrix.append(row)
    return matrix

# Create the bag-of-words matrix
bow_matrix = create_bow_matrix(tokenized_corpus, vocabulary)

# Convert to DataFrame for better visualization
df = pd.DataFrame(bow_matrix, columns=vocabulary)

print("Vocabulary (Feature Names):")
print(vocabulary)

print("\nBag of Words Matrix:")
print(df)

# Function to compute cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

# Compute cosine similarity matrix
cosine_sim_matrix = []
for i in range(len(bow_matrix)):
    cosine_sim_row = []
    for j in range(len(bow_matrix)):
        cosine_sim_row.append(cosine_similarity(bow_matrix[i], bow_matrix[j]))
    cosine_sim_matrix.append(cosine_sim_row)

# Print the cosine similarity matrix
print("\nCosine Similarity Matrix:")
print(pd.DataFrame(cosine_sim_matrix))

