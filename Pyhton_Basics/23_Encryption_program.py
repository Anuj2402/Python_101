import random 
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars) # converts the string to a list
key = chars.copy() # creates a copy of the chars list
random.shuffle(key) # shuffles the list in place

print("Encryption Program")
print(f"chars: {chars}")
print('\n')
print(f"Key: {key}")

#ENCRYPTION
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""
# for each letter in the plain text 
for letter in plain_text:
    index = chars.index(letter) # finds the index of the letter in chars
    cipher_text += key[index] # appends the corresponding letter from key to cipher_text

print(f"original text: {plain_text}")
print(f"Cipher text: {cipher_text}")



#DECRYPTION
oroginal_text = input("Enter the text to decrypt: ")
cipher_text = ""
# for each letter in the original text
for letter in oroginal_text:
    index = key.index(letter) # finds the index of the letter in key
    cipher_text += chars[index] # appends the corresponding letter from chars to cipher_text

print(f"original text: {oroginal_text}")
print(f"Cipher text: {cipher_text}")
