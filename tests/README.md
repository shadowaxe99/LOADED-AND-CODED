# Ultimate Chat to Code Bot Tests

This folder contains the tests for the Ultimate Chat to Code Bot project.

## test_bot.py


import unittest
from chatbot.bot import ChatBot

class TestChatBot(unittest.TestCase):
    def test_greeting(self):
        bot = ChatBot()
        response = bot.get_response("Hello")
        self.assertEqual(response, "Hi, how can I help you?")

    def test_farewell(self):
        bot = ChatBot()
        response = bot.get_response("Goodbye")
        self.assertEqual(response, "Goodbye! Have a great day.")

if __name__ == '__main__':
    unittest.main()


## test_nlp.py


import unittest
from chatbot.nlp import NLP

class TestNLP(unittest.TestCase):
    def test_tokenize(self):
        nlp = NLP()
        tokens = nlp.tokenize("This is a test sentence.")
        self.assertEqual(tokens, ["This", "is", "a", "test", "sentence."])

    def test_pos_tag(self):
        nlp = NLP()
        pos_tags = nlp.pos_tag("This is a test sentence.")
        self.assertEqual(pos_tags, [("This", "DT"), ("is", "VBZ"), ("a", "DT"), ("test", "NN"), ("sentence.", "NN")])

if __name__ == '__main__':
    unittest.main()


## test_web_surfing.py


import unittest
from chatbot.web_surfing import WebSurfing

class TestWebSurfing(unittest.TestCase):
    def test_search(self):
        web_surfing = WebSurfing()
        results = web_surfing.search("Python programming")
        self.assertEqual(len(results), 10)

    def test_get_title(self):
        web_surfing = WebSurfing()
        title = web_surfing.get_title("https://www.python.org/")
        self.assertEqual(title, "Welcome to Python.org")

if __name__ == '__main__':
    unittest.main()


## test_embedding_generation.py


import unittest
from embeddings.embedding_generation import EmbeddingGeneration

class TestEmbeddingGeneration(unittest.TestCase):
    def test_generate_embedding(self):
        embedding_generation = EmbeddingGeneration()
        embedding = embedding_generation.generate_embedding("This is a test sentence.")
        self.assertEqual(len(embedding), 300)

if __name__ == '__main__':
    unittest.main()

