import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
from typing import List

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()

    if word in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        p = get_close_matches(w, data.keys())[0]
        print("Did you mean %s instead?" % p)
        w2 = input("Press Y for yes and n for N : ")
        w2 = w2.lower()

        if w2 == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif w2 == "n":
            return "Word doesn't exist.Please double check it"
        else:
            return "We didnt undersatnd your query"

    else:
        return "Word doesn't exist.Please double check it"


word = input("Enter a word: ")

output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
