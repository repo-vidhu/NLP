import nltk
import re
from nltk.tokenize import word_tokenize

with open('file.txt', 'r') as file:
    data = file.read()

pattern = r'[^\w\s]|https?://\S+|www\.\S+'
punctuation_removed = re.sub(pattern=pattern, repl='', string=data)
tokens = word_tokenize(punctuation_removed)

# Get the total number of tokens and unique tokens
total_tokens = len(tokens)
set_tokens = set(tokens)

# Sort the set_tokens alphabetically
sorted_tokens = sorted(set_tokens)

print(f'Total Number of Tokens: {total_tokens}')
print(f'Total Number of Unique Tokens: {len(set_tokens)}')

# Print sorted word counts and percentages
for word in sorted_tokens:
    count = tokens.count(word)
    percentage = (count / total_tokens) * 100
    print(f'{word} :=> {count} times \t Percentage: {percentage:.2f}%')

