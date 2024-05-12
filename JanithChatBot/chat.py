import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #select device

with open('intents.json', 'r') as json_data:    # load intents file -> includes patterns
    intents = json.load(json_data) # List of dictornary

FILE = "data.pth"
data = torch.load(FILE) # Get saved model

# assign global variales
input_size = data["input_size"]         
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"] # parameters Bias terms & Weight values

#print("data ",data[''])
# Pass the pre-trained parameters
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state) 
model.eval()

bot_name = "Sam"
                        #return type ->
def get_response(msg:str) -> str:   # pass string model to get response
    sentence = tokenize(msg)    # tokenize the words
    X = bag_of_words(sentence, all_words)   # pass the bad of words # all words => 
    X = X.reshape(1, X.shape[0]) # Array into array
    X = torch.from_numpy(X).to(device)
    output = model(X) # Parameters of tensor object
    _, predicted = torch.max(output, dim=1)
   # print(" Tags ", tags)
    print(_, predicted) 

    # return the tag of model
    tag = tags[predicted.item()] #Get tag index of tag

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.5:
        for intent in intents['intents']: # List of dictornary
            if tag == intent["tag"]: #greeting == Tag
                return random.choice(intent['responses'])
    return "I do not understand..."


    