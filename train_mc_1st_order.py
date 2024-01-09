"""
Description: Training module of 1st order Markov Chain
             using nltk corpora from project gutenberg
"""
from Markov_Chain import MarkovChain
from nltk.corpus import gutenberg

# creating the chain 
# 1st order -> 0
MC = MarkovChain(0)

# any text file can be used to train the chain
corpora_path = 'C:\\Users\\ipart\\AppData\\Roaming\\nltk_data\\corpora\\gutenberg\\'

for filename in gutenberg.fileids():
    print(corpora_path+str('austen-emma.txt'))
    try:
        MC.train(corpora_path+str('austen-emma.txt'))
    except (UnicodeDecodeError):
        pass
     
# convert to json and save to file
MC.to_json('Markov Chain 1st order.json')



