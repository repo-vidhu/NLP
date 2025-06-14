import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import re

# Function to build vocabulary from the sentences
def build_vocabulary(sentences):
    # Create a set of all unique words in all sentences
    vocabulary = set()
    for sentence in sentences:
        words = preprocess_text(sentence)
        vocabulary.update(words)
    return sorted(vocabulary)

# Function to preprocess and tokenize sentences
def preprocess_text(text):
    # Remove non-alphanumeric characters, convert to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    words = text.split()
    return words

# Function to create a vector for each sentence based on the vocabulary
def create_vector(sentence, vocabulary):
    words = preprocess_text(sentence)
    word_count = Counter(words)
    
    # Create a vector based on the vocabulary
    vector = np.zeros(len(vocabulary))
    
    for i, word in enumerate(vocabulary):
        vector[i] = word_count.get(word, 0)
    
    return vector

# Function to find the most similar sentence
def find_most_similar_sentence(input_sentence, file_path):
    # Read the file content and split into sentences
    with open(file_path, 'r') as file:
        sentences = file.read().split('\n')
    
    # Build the vocabulary using the reference sentences
    vocabulary = build_vocabulary(sentences)
    
    # Create vectors for input sentence and all sentences from the file
    input_vector = create_vector(input_sentence, vocabulary)
    sentence_vectors = [create_vector(sentence, vocabulary) for sentence in sentences]
    
    # Compute cosine similarities between the input sentence and all other sentences
    similarities = cosine_similarity([input_vector], sentence_vectors)
    
    # Print the cosine similarity for each sentence
    for i, similarity in enumerate(similarities[0]):
        print(f"Similarity with sentence {i + 1}: {similarity}")
    
    # Find the index of the most similar sentence
    most_similar_index = np.argmax(similarities)
    most_similar_value = similarities[0][most_similar_index]  # Get similarity value of most similar sentence
    
    # Print similarity value of the most similar sentence
    print(f"Similarity value of the most similar sentence: {most_similar_value}")
    
    return sentences[most_similar_index]

# Example Usage
input_sentence = input("Enter the suitable input:")
file_path = '/home/cs-nn-14/vidhu/text5.txt'  

most_similar_sentence = find_most_similar_sentence(input_sentence, file_path)
print("Most similar sentence:", most_similar_sentence)

