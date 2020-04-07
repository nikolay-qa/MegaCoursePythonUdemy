import json
from pathlib import Path
from difflib import get_close_matches

data = json.load(open("data.json"))

def translator(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        user_i = input("Did you mean %s instead? Enter Y/N: " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if user_i == "Y":
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif user_i == "N":
            return "The word does not exist. Double check it."
        else:
            return "We do not understand your entry."
    else:
        return "This word does not exist. Please double check it."


word = input("Enter your word: ")
output = translator(word)
if type(output) == list:
    print("Your word's meaning is:\n", *output, sep='\n')
else:
    print(output)
