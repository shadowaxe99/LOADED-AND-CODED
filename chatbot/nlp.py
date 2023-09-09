import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLP:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        # Tokenize the text
        tokens = word_tokenize(text.lower())

        # Remove stop words
        tokens = [token for token in tokens if token not in self.stop_words]

        # Lemmatize the tokens
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]

        return tokens

    def get_embedding(self, text):
        # Preprocess the text
        tokens = self.preprocess_text(text)

        # Generate the embedding
        embedding = [len(token) for token in tokens]

        return embedding