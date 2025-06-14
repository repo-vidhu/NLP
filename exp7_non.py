import re
from collections import defaultdict
import math

# Step 1: Read and Preprocess the Tagged Data (Corpus)
def preprocess_tagged_data(data):
    """Process the tagged data into sentences with words and tags."""
    sentences = []
    for line in data:
        tokens = line.strip().split()
        sentence = []
        for token in tokens:
            word, tag = token.rsplit('/', 1)  # Split word and tag
            sentence.append((word, tag))
        sentences.append(sentence)
    return sentences

# Step 2: Train the HMM Model (Transition and Emission Probabilities)
def train_hmm(corpus):
    transition_probs = defaultdict(lambda: defaultdict(lambda: 0))
    emission_probs = defaultdict(lambda: defaultdict(lambda: 0))
    tag_counts = defaultdict(int)
    word_counts = defaultdict(int)
    
    # Iterate through the corpus to calculate the probabilities
    for sentence in corpus:
        previous_tag = None
        for word, tag in sentence:
            tag_counts[tag] += 1
            word_counts[word] += 1
            emission_probs[tag][word] += 1
            
            if previous_tag:
                transition_probs[previous_tag][tag] += 1
            previous_tag = tag
    
    # Convert counts to probabilities
    for prev_tag in transition_probs:
        total_transitions = sum(transition_probs[prev_tag].values())
        for tag in transition_probs[prev_tag]:
            transition_probs[prev_tag][tag] /= total_transitions
    
    for tag in emission_probs:
        total_emissions = sum(emission_probs[tag].values())
        for word in emission_probs[tag]:
            emission_probs[tag][word] /= total_emissions
    
    return transition_probs, emission_probs, tag_counts, word_counts

# Step 3: Viterbi Algorithm for POS Tagging
def viterbi(sentence, transition_probs, emission_probs, tag_counts, word_counts):
    # Initialize Viterbi table
    viterbi_table = [{}]
    backpointer = [{}]
    
    # Initialize base case
    for tag in tag_counts:
        viterbi_table[0][tag] = math.log(emission_probs[tag].get(sentence[0], 1e-10)) + math.log(1 / len(tag_counts))  # Assume uniform prior for the start
        backpointer[0][tag] = None
    
    # Fill the Viterbi table
    for i in range(1, len(sentence)):
        viterbi_table.append({})
        backpointer.append({})
        for tag in tag_counts:
            max_prob, prev_tag = max(
                [(viterbi_table[i-1][prev_tag] + math.log(transition_probs[prev_tag].get(tag, 1e-10)) + 
                  math.log(emission_probs[tag].get(sentence[i], 1e-10)), prev_tag) 
                 for prev_tag in tag_counts], 
                key=lambda x: x[0]
            )
            viterbi_table[i][tag] = max_prob
            backpointer[i][tag] = prev_tag
    
    # Backtrack to get the most probable sequence of tags
    best_tag_sequence = []
    best_last_tag = max(viterbi_table[-1], key=viterbi_table[-1].get)
    best_tag_sequence.append(best_last_tag)
    
    for i in range(len(sentence) - 1, 0, -1):
        best_tag_sequence.append(backpointer[i][best_tag_sequence[-1]])
    
    best_tag_sequence.reverse()
    
    return best_tag_sequence

# Step 4: Tag a New Sentence
def tag_sentence(sentence, transition_probs, emission_probs, tag_counts, word_counts):
    return viterbi(sentence, transition_probs, emission_probs, tag_counts, word_counts)

# Step 5: Main Logic (Train and Tag)
def main():
    # Example of reading tagged data (could be from file)
    data = ["I/PRP love/VBP programming/NN Python/NN is/VBZ awesome/JJ"]
    corpus = preprocess_tagged_data(data)
    
    # Train the HMM model
    transition_probs, emission_probs, tag_counts, word_counts = train_hmm(corpus)
    
    # Test sentence
    test_sentence = input("Enter the test sentence").split()
    
    # Tag the sentence
    tags = tag_sentence(test_sentence, transition_probs, emission_probs, tag_counts, word_counts)
    print(list(zip(test_sentence, tags)))

if __name__ == "__main__":
    main()

