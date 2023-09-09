
import numpy as np
import tensorflow as tf

def generate_embeddings(sentences):
    # Load pre-trained model
    model = tf.keras.models.load_model('embedding_model.h5')

    # Preprocess sentences
    preprocessed_sentences = preprocess_sentences(sentences)

    # Generate embeddings
    embeddings = model.predict(preprocessed_sentences)

    return embeddings

def preprocess_sentences(sentences):
    # Tokenize sentences
    tokenized_sentences = tokenize_sentences(sentences)

    # Pad sequences
    padded_sequences = pad_sequences(tokenized_sentences)

    return padded_sequences

def tokenize_sentences(sentences):
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(sentences)
    tokenized_sentences = tokenizer.texts_to_sequences(sentences)

    return tokenized_sentences

def pad_sequences(sequences):
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences)

    return padded_sequences

