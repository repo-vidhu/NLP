import re
import nltk
from nltk.text import Text
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import random

print("Downloading stopwords and wordnet....")
nltk.download('stopwords')
nltk.download('punkt')  # Ensure punkt is downloaded for tokenization
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')  # For POS tagging
print("Download complete!")

# Initialize lemmatizer and stemmer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Read the file and clean the lines
sentences = []
with open('text_concordance.txt', 'r') as file:
    lines = file.read()

for line in lines.split('\n'):  # Split by line instead of character by character
    punctuation_removed = re.sub(pattern='[^\w\s]', repl='', string=line)
    sentences.append(punctuation_removed)

# Get stopwords and clean the tokens
stop_words = set(stopwords.words('english'))
tokens = [word for sentence in sentences for word in sentence.split() if word.lower() not in stop_words]

# Apply stemming first
stemmed_tokens = [stemmer.stem(word) for word in tokens]

# Perform POS tagging on the stemmed tokens
tagged_tokens = nltk.pos_tag(stemmed_tokens)

# Define a function to get the appropriate POS for lemmatization
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return 'a'  # adjective
    elif tag.startswith('V'):
        return 'v'  # verb
    elif tag.startswith('N'):
        return 'n'  # noun
    elif tag.startswith('R'):
        return 'r'  # adverb
    else:
        return 'n'  # default to noun if not found

# Lemmatize the tokens based on POS tags
lemmatized_tokens = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) for word, tag in tagged_tokens]

# Create the Text object for concordance
text = Text(lemmatized_tokens)

# Select a random word from the tokens
random_word = random.choice(lemmatized_tokens)

# Output the selected word
print(f"Randomly selected word: {random_word}")

# Ask the user for context (number of words)
context_words = int(input('Enter the number of context words: '))

# Define a function to show concordance with context words and highlight the target word
def concordance_with_words(text, word, context_words):
    word_indexes = [i for i, w in enumerate(text) if w == word]
    concordance_lines = []
    for index in word_indexes:
        start = max(0, index - context_words)
        end = min(len(text), index + context_words + 1)
        concordance_line = ' '.join(text[start:index] + ['[' + word + ']'] + text[index + 1:end])
        concordance_lines.append(concordance_line)
    return concordance_lines

# Show concordance for the randomly selected word
concordance_lines = concordance_with_words(lemmatized_tokens, random_word, context_words)
for line in concordance_lines:
    print(line)

