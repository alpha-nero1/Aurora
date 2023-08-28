import pickle

"""
    Load the knowledgebase file.
"""
def load_kb():
    with open('./data/knowledgebase.txt', 'r') as f:
        return f.read().split('\n')
    

"""
    Train the model.
"""
def train():
    data = load_kb()

train()