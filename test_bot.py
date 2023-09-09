import unittest
from chatbot.bot import ChatBot

class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.bot = ChatBot()

    def test_greeting(self):
        response = self.bot.get_response("Hello")
        self.assertEqual(response, "Hi, how can I assist you?")

    def test_question(self):
        response = self.bot.get_response("What is the weather today?")
        self.assertIn("weather", response)

    def test_goodbye(self):
        response = self.bot.get_response("Goodbye")
        self.assertEqual(response, "Goodbye! Have a nice day.")

if __name__ == '__main__':
    unittest.main()