# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:
# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

#     # ord() function returns the Unicode code from a given character.
#     # chr() function is the inverse of ord() function. It converts the Unicode code for a character into a character itself.

def encrypt(text, shift):
    cypher_text = ""
    for letter in text:
        if letter.isalpha():
            ascii_offset = ord('A') if letter.isupper() else ord('a')
            cypher_text += chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            cypher_text += letter
    return cypher_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

        another = input("Do you want to perform another operation? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()


