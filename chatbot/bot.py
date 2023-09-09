class ChatBot:
    def __init__(self):
        self.name = "Ultimate ChatBot"

    def greet(self):
        print(f"Hello! I am {self.name}, your ultimate chatbot.")

    def chat(self, message):
        if message.lower() == "hello":
            print("Hi there!")
        elif message.lower() == "how are you?":
            print("I'm doing great, thank you!")
        else:
            print("I'm sorry, I don't understand.")

bot = ChatBot()
bot.greet()
user_input = input("Enter your message: ")
bot.chat(user_input)