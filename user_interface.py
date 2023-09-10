import tkinter as tk
from bot import ChatBot

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.chatbot = ChatBot()
        self.conversation = tk.Text(self.root)
        self.message = tk.Entry(self.root)
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)

    def send_message(self):
        # Get the user's message
        user_message = self.message.get()

        # Clear the message box
        self.message.delete(0, tk.END)

        # Display the user's message
        self.conversation.insert(tk.END, "You: " + user_message + "\n")

        # Get the chatbot's response
        chatbot_response = self.chatbot.chat(user_message)

        # Display the chatbot's response
        self.conversation.insert(tk.END, "ChatBot: " + chatbot_response + "\n")

    def run(self):
        # Pack the widgets
        self.conversation.pack()
        self.message.pack()
        self.send_button.pack()

        # Start the GUI
        self.root.mainloop()