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
    word_count = {}

    # Count occurrences of each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Create a vector based on the vocabulary
    vector = [0] * len(vocabulary)
    
    for i, word in enumerate(vocabulary):
        vector[i] = word_count.get(word, 0)
    
    return vector

# Function to compute cosine similarity between two vectors
def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude_v1 = sum(a * a for a in v1) ** 0.5
    magnitude_v2 = sum(b * b for b in v2) ** 0.5
    
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0
    
    return dot_product / (magnitude_v1 * magnitude_v2)

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
    similarities = []
    for sentence_vector in sentence_vectors:
        similarities.append(cosine_similarity(input_vector, sentence_vector))
    
    # Find the index of the most similar sentence
    most_similar_index = similarities.index(max(similarities))
    
    return sentences[most_similar_index]

# Example Usage
input_sentence = input("Enter the suitable input:")
file_path = '/home/cs-nn-14/vidhu/exp5.txt'  

most_similar_sentence = find_most_similar_sentence(input_sentence, file_path)
print("Most similar sentence:", most_similar_sentence)

