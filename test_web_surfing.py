import unittest
from chatbot.web_surfing import WebSurfing

class TestWebSurfing(unittest.TestCase):
    def setUp(self):
        self.web_surfing = WebSurfing()

    def test_search(self):
        query = "python"
        result = self.web_surfing.search(query)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_get_page_content(self):
        url = "https://www.example.com"
        result = self.web_surfing.get_page_content(url)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()