"""Decrypts your messages"""


import sys

# Define the original and encrypted alphabets
lower = 'abcdefghijklmnopqrstuvwxyz'
alphabets = lower + lower.upper()
cyrillic_alphabet = 'абвгдеёжзийклмнопрстуфхцчш'
greek_alphabet = '\u03B1\u03B2\u03B3\u03B4M\u03B6\u03B7\u03B8X\u03BA\u03BB\u03BC\u03BD\u03BE\u03BF\u03C0\u03C1\u03C3\u03C4Z\u03C6\u03C7J\u03C9LS'
encrypted_alphabets = cyrillic_alphabet + greek_alphabet

# Decrypts messages using predefined rules
def decrypt_text(text):
    decrypted_string = ''

    for letter in text:
        if letter in encrypted_alphabets:
            index = encrypted_alphabets.index(letter)
            decrypted_string += alphabets[index]
        else:
            decrypted_string += letter

    return decrypted_string

# Decrypts the encrypted file
def decrypt_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, "r", encoding="utf-8") as input_file:
            input_text = input_file.read()
        
        decrypted_text = decrypt_text(input_text)

        with open(output_file_path, "w") as output_file:
            output_file.write(decrypted_text)

        print("Decryption successful! Reopen {}.".format(output_file_path))

    except FileNotFoundError:
        print("Error: {} was not found in the directory.".format(input_file_path))


#Get file inputs from the user
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decryption.py input_file")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = input_file_path

    decrypt_file(input_file_path, output_file_path)
