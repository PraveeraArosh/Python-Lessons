import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    """
    split sentence into array of words/tokens 
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence) # sentence eka vachana valata kadanava
# return type - List []


def stem(word): # find root word 
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32) # tokensize word vala length valata hriynna bag of words hadenva
    for idx, w in enumerate(words): # enumerate -> [index : value]
        if w in sentence_words: # tokenize sentence vala thiyena value eka samana da kiyala balanava
            bag[idx] = 1

    return bag


words = ["organize", "organizes", "organizing"] # word List
print(words)
words = [stem(w) for w in words] # get words one by one into w variable
print(words)