import unittest
from chatbot.nlp import NLP

class TestNLP(unittest.TestCase):
    def setUp(self):
        self.nlp = NLP()

    def test_tokenize(self):
        text = "Hello, how are you?"
        expected_tokens = ["Hello", ",", "how", "are", "you", "?"]
        tokens = self.nlp.tokenize(text)
        self.assertEqual(tokens, expected_tokens)

    def test_remove_stopwords(self):
        tokens = ["Hello", ",", "how", "are", "you", "?"]
        expected_filtered_tokens = ["Hello", ",", "?"]
        filtered_tokens = self.nlp.remove_stopwords(tokens)
        self.assertEqual(filtered_tokens, expected_filtered_tokens)

    def test_stemming(self):
        tokens = ["Hello", ",", "how", "are", "you", "?"]
        expected_stemmed_tokens = ["hello", ",", "how", "are", "you", "?"]
        stemmed_tokens = self.nlp.stemming(tokens)
        self.assertEqual(stemmed_tokens, expected_stemmed_tokens)

if __name__ == '__main__':
    unittest.main()