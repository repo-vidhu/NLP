import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Function to get synonym for a word
def get_synonym(word):
    # Get word synonyms from WordNet
    synsets = wn.synsets(word)
    if synsets:
        # Return the first synonym found
        for lemma in synsets[0].lemmas():
            if lemma.name() != word:
                return lemma.name()
    return word

# Function to get antonym for a word
def get_antonym(word):
    # Get antonyms from WordNet
    synsets = wn.synsets(word)
    for syn in synsets:
        for lemma in syn.lemmas():
            if lemma.antonyms():
                return lemma.antonyms()[0].name()
    return word  # If no antonym is found, return the word itself

# Function to handle negation
def handle_negation(word, is_negation):
    if is_negation:
        return get_antonym(word)  # Negate the word after 'not'
    else:
        return get_synonym(word)  # Replace with synonym

# Function to replace words with synonyms and negation with antonyms
def replace_with_synonyms_and_antonyms(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    
    # Create a list to store modified words
    modified_words = []
    is_negation = False  # Flag to track negations
    
    # Process each word in the sentence
    for i, word in enumerate(words):
        word_lower = word.lower()
        
        # If the word is 'not', flag it as a negation
        if word_lower == 'not':
            is_negation = True
            modified_words.append(word)
        elif word_lower in stop_words:  # Skip stop words
            modified_words.append(word)
            is_negation = False  # Reset negation flag
        else:
            # Handle negation or synonym replacement
            modified_word = handle_negation(word, is_negation)
            modified_words.append(modified_word)
            is_negation = False  # Reset negation flag after processing
    
    # Detokenize the words to form a complete sentence
    return TreebankWordDetokenizer().detokenize(modified_words)

# Example usage
input_text = "The quick fox is not lazy and jumps over the dog."
output_text = replace_with_synonyms_and_antonyms(input_text)

print("Original Text:", input_text)
print("Modified Text:", output_text)

