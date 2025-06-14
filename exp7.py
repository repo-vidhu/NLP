import nltk
import re
from nltk.corpus import stopwords, wordnet, treebank
from nltk.tag import PerceptronTagger
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('treebank')

lemmatizer = WordNetLemmatizer()

# Define part-of-speech tags
pos_tags = {
    "CC": "Coordinating conjunction",
    "CD": "Cardinal number",
    "DT": "Determiner",
    "EX": "Existential there",
    "FW": "Foreign word",
    "IN": "Preposition or subordinating conjunction",
    "JJ": "Adjective",
    "JJR": "Adjective, comparative",
    "JJS": "Adjective, superlative",
    "LS": "List item marker",
    "MD": "Modal",
    "NN": "Noun, singular or mass",
    "NNS": "Noun, plural",
    "NNP": "Proper noun, singular",
    "NNPS": "Proper noun, plural",
    "PDT": "Predeterminer",
    "POS": "Possessive ending",
    "PRP": "Personal pronoun",
    "PRP$": "Possessive pronoun",
    "RB": "Adverb",
    "RBR": "Adverb, comparative",
    "RBS": "Adverb, superlative",
    "RP": "Particle",
    "SYM": "Symbol",
    "TO": "To (as part of an infinitive verb)",
    "UH": "Interjection",
    "VB": "Verb, base form",
    "VBD": "Verb, past tense",
    "VBG": "Verb, gerund or present participle",
    "VBN": "Verb, past participle",
    "VBP": "Verb, non-3rd person singular present",
    "VBZ": "Verb, 3rd person singular present",
    "WDT": "Wh-determiner",
    "WP": "Wh-pronoun",
    "WP$": "Possessive wh-pronoun",
    "WRB": "Wh-adverb"
}

def get_file(path):
    sentences = []
    with open(path, 'r') as f:
        sentence = f.readlines()
        sentences = [s.strip() for s in sentence]
    return sentences

def get_tag(word):
    """Determine the WordNet POS tag"""
    if word.startswith('J'):
        return wordnet.ADJ
    elif word.startswith('V'):
        return wordnet.VERB
    elif word.startswith('N'):
        return wordnet.NOUN
    elif word.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

stop_words = set(stopwords.words('english'))

def preprocess(data, tagger):
    print("_"*60)
    print(f"Original Data: {data}")
    
    # Clean data: Remove unwanted characters like punctuation
    tokens = re.findall(r'\b\w+\b', data.lower())  # Extract words and lowercasing them
    tokens = [token for token in tokens if token not in stop_words]

    # Tag the tokens using the provided tagger
    tagged_tokens = tagger.tag(tokens)
    print("_"*60)

    for word, tag in tagged_tokens:
        print(f"{word}\t=> {pos_tags.get(tag, 'Unknown')}\t=> {tag}")

    l = []
    for word, tag in tagged_tokens:
        w = lemmatizer.lemmatize(word, get_tag(tag))
        l.append(w)
    print('\n')
    
    return tagged_tokens, l

# Load the PerceptronTagger
tagger = PerceptronTagger()

data = get_file('text6.txt')
a = []
l = []

# Preprocess each line in the data
for d in data:
    if d.strip():  # Ensure the line is not empty
        k, m = preprocess(d, tagger)
        a.extend(k)
        l.append(m)
