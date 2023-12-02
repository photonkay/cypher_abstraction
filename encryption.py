"""Encrypts your messages"""


import sys

# Define the original and encrypted alphabets
lower = 'abcdefghijklmnopqrstuvwxyz'
alphabets = lower + lower.upper()
cyrillic_alphabet = 'абвгдеёжзийклмнопрстуфхцчш'
greek_alphabet = '\u03B1\u03B2\u03B3\u03B4M\u03B6\u03B7\u03B8X\u03BA\u03BB\u03BC\u03BD\u03BE\u03BF\u03C0\u03C1\u03C3\u03C4Z\u03C6\u03C7J\u03C9LS'
encrypted_alphabets = cyrillic_alphabet + greek_alphabet

# Encrypts the text using predefined rules
def encrypt_text(text):
    encrypted_string = ''

    for letter in text:
        if letter.isalpha():
            index = alphabets.index(letter)
            encrypted_string += encrypted_alphabets[index]
        else:
            encrypted_string += letter
    return encrypted_string

# encrypts texts from a file, and outputs into a separate file
def encrypt_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, "r") as input_file:
            input_text = input_file.read()
        
        encrypted_text = encrypt_text(input_text)

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(encrypted_text)

        print("{} has been encrypted into {}.".format(input_file_path, output_file_path))
    except FileNotFoundError:
        print("Error: {} was not found in the directory.".format(input_file_path))
    except Exception as e:
        print(f"Encountered an error: {e}")

#Get file inputs from the user
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encryption.py input_file output_file")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    encrypt_file(input_file_path, output_file_path)
