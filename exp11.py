from sklearn.feature_extraction.text import TfidfVectorizer

def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def compute_tfidf(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    
    for doc_idx, doc in enumerate(documents):
        print(f"Document {doc_idx+1}:")
        print(f"Document contents:{doc}\n")
        print("TF-IDF value :")
        
        for word_idx, word in enumerate(feature_names):
            tfidf_value = tfidf_matrix[doc_idx, word_idx]
            if tfidf_value > 0:
                print(f"  {word}: {tfidf_value:.4f}")
        print("\n")

if __name__ == "__main__":
    file_path = "exp11.txt"  # Change this to your actual file path
    documents = read_document(file_path)
    compute_tfidf(documents)

