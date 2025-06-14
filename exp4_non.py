import string

# Read the file and clean the lines
sentences = []
with open('text_concordance.txt', 'r') as file:
    lines = file.read()

# Function to remove punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Function to tokenize text
def tokenize(text):
    return text.split()

# Function to remove stopwords
def remove_stopwords(tokens, stop_words):
    return [word for word in tokens if word.lower() not in stop_words]

# List of stopwords
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Clean and tokenize the lines
tokens = []
for line in lines.split('\n'):
    punctuation_removed = remove_punctuation(line)
    line_tokens = tokenize(punctuation_removed)
    cleaned_tokens = remove_stopwords(line_tokens, stop_words)
    sentences.append(cleaned_tokens)
    tokens.extend(cleaned_tokens)

# Select a random word from the tokens
import random
random_word = random.choice(tokens)

# Output the selected word
print(f"Randomly selected word: {random_word}")

# Ask the user for context (width of the concordance)
context = int(input('Enter the context width: '))

# Function to show concordance for the selected word
def concordance(word, tokens, width):
    concordance_lines = []
    for i, token in enumerate(tokens):
        if token == word:
            start = max(0, i - width)
            end = min(len(tokens), i + width + 1)
            concordance_line = {
                'line_number': i,
                'context': ' '.join(tokens[start:end])
            }
            concordance_lines.append(concordance_line)
    return concordance_lines

# Show concordance for the randomly selected word
concordance_lines = concordance(random_word, tokens, context)

# Structured output
print("\nConcordance Results:")
for line in concordance_lines:
    print(f"Line {line['line_number']}: {line['context']}")

