import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import tree2conlltags

# Step 1: Download NLTK resources
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Sample text
text = "Elon Musk founded SpaceX in Hawthorne, California, and he is also the CEO of Tesla. "

# Step 2: Tokenize and tag parts of speech
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Step 3: Perform Named Entity Recognition (NER)
ner_tree = ne_chunk(tagged)

# Step 4: Convert the NER tree into a list of named entities
named_entities = tree2conlltags(ner_tree)	# convert the parsed tree into a format that is easier to work with.

# Display named entities
print("Named Entities:")
for entity in named_entities:
    if entity[2] != 'O':  # Filter out non-entities
        print(f"Entity: {entity[0]} | Type: {entity[2]}")

# Step 5: Extract relationships between named entities (basic example)
# A simple relationship extraction using context and co-occurrence
print("\nExtracted Relations:")
entities = [entity[0] for entity in named_entities if entity[2] != 'O']
relationships = []

for i in range(len(entities)-1):
    relationships.append(f"{entities[i]} <-> {entities[i+1]}")

for relation in relationships:
    print(relation)

