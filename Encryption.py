from collections import OrderedDict

def main():
    option = input ("would you like to encrypt or decrypt (e or d): ")

    if (option == "e"):
        encrypt()
    elif (option == "d"):
        decrypt()

def encrypt():
    userInput = input("what would you like to encrypt: ")
    key = input("what key would you like to use?: ")
    encyrpted = cypher(userInput, key)

def decrypt():
    userInput = input("what would you like to decrypt: ")

def cypher(input, key):
    # Cleanse our key of any Duplicate Letters
    # This is used as the key for our cypher
    cleansedKey = "".join(OrderedDict.fromkeys(key))

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

    print (alphabet)




main()