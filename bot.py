from nlp import NLP
from machine_learning import MachineLearning

class ChatBot:
    def __init__(self):
        self.name = "Ultimate ChatBot"
        self.nlp = NLP()
        self.ml = MachineLearning()

    def greet(self):
        print(f"Hello! I am {self.name}, your ultimate chatbot.")

    def chat(self, message):
        # Preprocess the message
        tokens = self.nlp.preprocess_text(message)

        # Generate the response
        response = self.ml.predict(tokens)

        print(response)

bot = ChatBot()
bot.greet()
user_input = input("Enter your message: ")
bot.chat(user_input)