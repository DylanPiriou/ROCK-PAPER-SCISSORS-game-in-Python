import random
import string

CHARS = list(string.punctuation + string.whitespace + string.digits + string.ascii_letters)
SHUFFLE_CHARS = CHARS.copy()
random.shuffle(SHUFFLE_CHARS)

text = input("Enter your message: ")
encrypted_text = ""
for letter in text:
    index = CHARS.index(letter)
    encrypted_text += SHUFFLE_CHARS[index]
print(f"{encrypted_text}")


