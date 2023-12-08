#! /usr/bin/python3

"""Script to encrypt and decrypt"""


import argparse
import ast


def generate_key():
    # Mapping each letter to a symbol
    symbols = ':#&ⴕ~|έ^$`‡_@*%=-ⴃ+</0>∞Xⴣ'
    key = dict(zip("abcdefghijklmnopqrstuvwxyz", symbols))
    return key


def encrypt(message, key):
    encrypted_message = []
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            encrypted_char = key[char.lower()]
            encrypted_message.append((encrypted_char, is_upper))
        else:
            encrypted_message.append((char, None))  # Non-alphabet characters
    return encrypted_message


def decrypt(encrypted_message, key):
    decrypted_message = []
    for char, is_upper in encrypted_message:
        if is_upper is not None:
            for ref, value in key.items():
                if char == value:
                    decrypted_char = ref
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)  # Non-alphabet characters
    return "".join(decrypted_message)


def main():
    key = generate_key()

    parser = argparse.ArgumentParser(
        prog='Pepae',
        description="Uses a key to encrypt and decrypt messages.",
        epilog="This is how Pepae works")

    parser.add_argument(
        '--version', action='version', version='%(prog)s 2.0',
        help='Check version of Pepae on your device')
    parser.add_argument(
        '-e', '--encrypt', help='Flag to encrypt messasges',
        nargs=2, metavar=("INPUT_FILE", "OUTPUT_FILE"))
    parser.add_argument(
        '-d', '--decrypt', help='Flag to decrypt messasges',
        nargs=1, metavar=("INPUT_FILE"))

    args = parser.parse_args()

    if args.encrypt:
        input_file, output_file = args.encrypt

        try:
            with open(input_file, 'r', encoding='utf-8') as in_file:
                text = in_file.read()
                encrypted_text = encrypt(text, key)
                with open(output_file, 'w', encoding='utf-8') as out_file:
                    out_file.write(str(encrypted_text))
                print(f"Encryption successful. See {output_file}")
        except FileNotFoundError:
            print(f"Umm {input_file} not found.")
        except IOError:
            print("Error: Unable to write to the output file.")

    if args.decrypt:
        input_file = args.decrypt[0]

        try:
            with open(input_file, 'r', encoding='utf-8') as in_file:
                encrypted_message = ast.literal_eval(in_file.read())
                decrypted_text = decrypt(encrypted_message, key)
                with open(input_file, 'w', encoding='utf-8') as out_file:
                    out_file.write(str(decrypted_text))
                print(f"Decryption success! Reopen {input_file}")
        except FileNotFoundError:
            print(f"Umm {input_file} not found.")
        except IOError:
            print("Error: Unable to write to the output file.")


if __name__ == "__main__":
    main()
