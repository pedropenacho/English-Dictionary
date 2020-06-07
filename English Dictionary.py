import json
from difflib import get_close_matches

dictionary = json.load(open("data.json"))

def wordConsulting(word):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    elif word.title() in dictionary: #if user entered "texas" this will check for "Texas" as well.
        return dictionary[word.title()]
    elif word.upper() in dictionary: #in case user enters words like USA or NATO
        return dictionary[word.upper()]
    elif len(get_close_matches(word, dictionary.keys(), cutoff=0.7)) > 0:
        answer = input("Did you mean %s instead. \nPlease enter Y if yes, or N if no: " % get_close_matches(word, dictionary.keys())[0])
        if answer.lower() == "y":
            return dictionary[get_close_matches(word, dictionary.keys())[0]]
        elif answer.lower() == "n":
            return "\nThe word doesn't exist. Please double check it."
        else:
            return "\nWe didn't understand your entry."
    else:
        return "\nThe word doesn't exist. Please double check it."

word = input("Enter word: ")

definitions = wordConsulting(word)

if isinstance(definitions, list):
    print("Meaning:")
    for definition in definitions:
        print(str(definitions.index(definition) + 1) + ". "  + definition)
else:
    print(definitions)

close = False

while not close:

    closeConsole = input("\n\nDo you want to close dictionary? Please enter Y if yes, or N if you wish to look for another word: ")

    if closeConsole.lower() != "y" and closeConsole.lower() != "n":
        print("We didn't understand your entry.")
    elif closeConsole.lower() == "n":
        newWord = input("\nEnter word: ")
        definitions = wordConsulting(newWord)

        if isinstance(definitions, list):
            print("Meaning:")
            for definition in definitions:
                print(str(definitions.index(definition) + 1) + ". " + definition)
        else:
            print(definitions)
    else:
        close = True
     