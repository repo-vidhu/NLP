import re
import string
import nltk
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import contractions


def download_nltk_resources():
    try:
        stop_words = set(stopwords.words('english'))
    except LookupError:
        nltk.download('stopwords')
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

download_nltk_resources()

file=open('text1.txt', 'r')
tweets = file.readlines()
print("\n\n")
print(f"The tweets initially present in the file is:\n{tweets}")

def convert_to_lowercase(text):
    return text.lower()
    
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
    
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = word_tokenize(text)
    return ' '.join([word for word in words if word not in stop_words])
stemmer = PorterStemmer()
def stem_text(text):
    words = word_tokenize(text)
    return ' '.join([stemmer.stem(word) for word in words])

lemmatizer = WordNetLemmatizer()
def lemmatize_text(text):
    words = word_tokenize(text)
    return ' '.join([lemmatizer.lemmatize(word) for word in words])

def remove_emojis(text):
    return re.sub(r'[^\w\s,.!?]', '', text)

def remove_urls(text):
    return re.sub(r'http\S+|www\S+', '', text)

def replace_contractions(text):
    return contractions.fix(text)


def process_tweet(text):
    print("\nOriginal tweet:")
    print(text)
    
    text = convert_to_lowercase(text)
    print("After converting to lowercase:")
    print(text)
    
    text = remove_punctuation(text)
    print("After removing punctuation:")
    print(text)
    
    text = remove_urls(text)
    print("After removing URLs:")
    print(text)
    
    text = remove_emojis(text)
    print("After removing emojis:")
    print(text)
    
    text = replace_contractions(text)
    print("After replacing contractions:")
    print(text)
    
    text = remove_stopwords(text)
    print("After removing stopwords:")
    print(text)
    text1=text
    text = stem_text(text)
    print("After stemming:")
    print(text)
    
    text = lemmatize_text(text1)
    print("After lemmatization:")
    print(text)
    
    return text


processed_tweets = [process_tweet(tweet) for tweet in tweets]

print("\n\n")
print("The final processed tweets are:")
print(processed_tweets)
