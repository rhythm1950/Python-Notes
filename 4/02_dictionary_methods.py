myDict = {
    "fast": "In a Quick Manner",
    "rhythm": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'rhythm': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "rhythm": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("rhythm")) # Prints value associated with key "rhythm"
print(myDict["rhythm"]) # Prints value associated with key "rhythm"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("rhythm2")) # Returns None as rhythm2 is not present in the dictionary
print(myDict["rhythm2"]) # throws an error as rhythm2 is not present in the dictionary