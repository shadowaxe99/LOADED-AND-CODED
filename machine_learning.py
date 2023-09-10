from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import numpy as np

class MachineLearning:
    def __init__(self):
        self.model = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('classifier', DecisionTreeClassifier())
        ])
        self.intents = ['hello', 'how are you', 'what is your name', 'goodbye']
        self.responses = ['Hello!', 'I am doing great, thank you.', 'I am Ultimate ChatBot.', 'Goodbye!']

    def train(self, data):
        # Extract the intents and responses from the data
        for intent, response in data:
            self.intents.append(intent)
            self.responses.append(response)

        # Train the model
        self.model.fit(self.intents, self.responses)

    def predict(self, input):
        # Predict the index of the best response
        index = self.model.predict([input])[0]

        # Return the best response
        return self.responses[index]