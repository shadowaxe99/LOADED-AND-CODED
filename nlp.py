import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from textblob import TextBlob

class NLP:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
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

    def get_pos_tags(self, tokens):
        # Get the POS tags
        pos_tags = pos_tag(tokens)

        return pos_tags

    def get_named_entities(self, tokens):
        # Get the named entities
        named_entities = ne_chunk(pos_tag(tokens))

        return named_entities

    def get_sentiment(self, text):
        # Get the sentiment
        sentiment = TextBlob(text).sentiment

        return sentiment

    def get_embedding(self, text):
        # Preprocess the text
        tokens = self.preprocess_text(text)

        # Generate the embedding
        embedding = [len(token) for token in tokens]

        return embedding