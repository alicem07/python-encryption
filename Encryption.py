from collections import OrderedDict

def main():
    userInput = input("what would you like to encrypt: ")
    key = input("what key would you like to use?: ")
    encyrpted = cypher(userInput, key)

    # Print our Encyption
    print("Here is your encyrpted phase: " + encyrpted)

def cypher(input, key):
    # Remove whitespace from our key
    key = key.replace(' ', '')

    # Cleanse our key of any Duplicate Letters
    # This is used as the key for our cypher
    # Convert all uppercase letter to lowercase letters in our key
    cleansedKey = "".join(OrderedDict.fromkeys(key)).lower()

    # Generate our Alphabet for the cypher
    alphabet = []

    # Add our cleansed key to the beginning of our alphabet
    for letter in cleansedKey:
        alphabet.append(letter)

    # Add the rest of the letters to the alphabet
    for letter in range(ord('a'), ord('z') + 1):
        character = chr(letter)
        if character not in alphabet:
            alphabet.append(character)

    outputCyphered = ""

    for letter in input:
        # Check if letter is a space
        if letter == ' ':
            outputCyphered = outputCyphered + letter
        else:
            # Subtract the integer representation of a from the letter to get
            # the position in the alphabet (0-25)
            alphabetPosition = ord(letter) - ord('a')

            # Replace our letter with the equivalent position from our
            # cyphered alphabet
            cypheredLetter = alphabet[alphabetPosition]

            outputCyphered = outputCyphered + cypheredLetter
    
    return outputCyphered

main()