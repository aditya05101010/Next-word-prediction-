
from Markov_Chain import MarkovChain
import sys

def load_markov_chain(order):
    """
    Loads the trained markov chain
    """
    if order == "1":
        try:
            new_chain = MarkovChain.from_json('Markov Chain 1st order.json')
            print("Markov Chain 1st order is loaded Successfully.")
            return new_chain
        except (FileNotFoundError):
            print("Couldn't load the Markov Chain 1st order. File does not exist.")
            print("First train a Markov Chain 1st order and save it to a json file.")
            print("See 'train_markov_chain_1st_order.py' file ")
            sys.exit(0)
    elif order == "2":
        try:
            new_chain = MarkovChain.from_json('Markov Chain 2nd order.json')
            print("Markov Chain 2nd order is loaded Successfully.")
            return new_chain
        except (FileNotFoundError):
            print("Couldn't load the Markov Chain 2nd order. File does not exist.")
            print("First train a Markov Chain 2nd order and save it to a json file.")
            print("(See 'train_markov_chain_2nd_order.py' file )")
            sys.exit(0)
    elif order == "3":
        try:
            new_chain = MarkovChain.from_json('Markov Chain 3rd order.json')
            print("Markov Chain 3rd order is loaded Successfully.")
            return new_chain
        except (FileNotFoundError):
            print("Couldn't load the Markov Chain 3rd order. File does not exist.")
            print("First train a Markov Chain 3rd order and save it to a json file.")
            print("(See 'train_markov_chain_3rd_order.py' file)")
            sys.exit(0)
    else:
        print("Wrong Input")
        print("Type 1 to load 1st order Markov Chain")
        print("Type 2 to load 2nd order Markov Chain")
        print("Type 3 to load 3rd order Markov Chain")
        sys.exit(0)

def predict_next_word(state, chain, order):
    """
    Predicts the next word that will be typed.
    Input: string -> word or words that the user typed.
           the words that the user typed determine the current state at the
           chain. For a first order markov chain just the last word the user 
           typed is considered. For a second order markov chain the last two 
           words the user typed are considered etc.
           chain -> markov chain object 
    Return: string -> predicted word
    """
    if order == "1":
        print("... " + state[-1] + " ...")
        prediction = chain.find_next_state(state[-1])
        return prediction
    elif order == "2":
        print("... " + " ".join(state[-2:]) + " ...")
        prediction = chain.find_next_state(" ".join(state[-2:]))
        return prediction
    elif order == "3":
        print("... " + " ".join(state[-3:]) + " ...")
        prediction = chain.find_next_state(" ".join(state[-3:]))
        return prediction
    else:
        print("Something went wrong. Prediction failed")
    
    

# user's input
typed = []
quit = False

order = input("Choose Markov Chain order (1,2,3) : ")
while order not in ["1","2","3"]:
  print("Wrong Input, Please choose from Type 1,2 or 3 respectively.")
  print("Type 1 to load 1st order Markov Chain")
  print("Type 2 to load 2nd order Markov Chain")
  print("Type 3 to load 3rd order Markov Chain")
  order = input("Choose Markov Chain order (1,2,3) : ")

chain = load_markov_chain(order)
print("--------------------------------------------------------")
print("Type below : ")
print("Your input must be at least {num} words".format(num=order))
print("When you want to get a next word prediction, please Press 'Enter'.")
print("--------------------------------------------------------")

## taking user input
while quit == False:
    print("\n(To exit press 'q')")
    word = input("Type here --> ").split()
    typed.extend(word[:])
    if typed[-1] == 'q':
        quit = True
        break
    else:
        next_word = predict_next_word(typed,chain,order)
        print("Prediction :    {nw}".format(nw = next_word))

# exiting
save = input("Do you wish to save your input? (y/n) ")
if save in ['y', 'yes', 'YES', 'Y']:
    with open("user_input.txt","w") as f:
        f.write(' '.join(typed[:-1]))  

retrain = input("Do you wish to retrain the chain with your input? (y/n) ")
if retrain in ['y', 'yes', 'YES', 'Y']:
    try: 
        chain.train("user_input.txt")
    except (UnicodeDecodeError):
        print("Unable to open file")
        
    
