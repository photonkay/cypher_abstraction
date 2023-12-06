# Pepae: StayingCoded

Pepae (pronounced as pep) is developed by us to encrypt and decrypt our messages. Our goal is to be shady.

## Features
- **Encryption:** Convert plain text messages into encrypted tuple texts.
- **Decryption:** Decrypt previously encrypted messages to retrieve the original.

## Help
You can use the command:
```bash
python pepae.py -h
```
or
```bash
python pepae.py --help
```
to learn the usage of pepae. Nonetheless, below is the usage

## Usage

### Encryption
To encrypt a message, use the following command:

```bash
python pepae.py -e input_file_path output_file_path
```
or
```bash
python pepae.py --encrypt input_file_path output_file_path
```
- `input_file_path`: The path to the file containing the message you want to encrypt.
- `output_file_path`: The path where the encrypted message will be saved.

### Decryption
To decrypt a message, use the following command:

```bash
python pepae.py -d input_file_path
```
or
```bash
python pepae.py --decrypt input_file_path
```
- `input_file_path`: The path to the file containing the encrypted message.
Note (Automagically): The encrypted file is overwritten with the decrypted. Works like magic.

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/photonkay/cypher_abstraction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pepae
    ```

3. Encrypt or Decrypt as specified in the usage


## Contributors
- photonkay
- Enoch1357

Enjoy the secured communication, all thanks to PEPAE! Happy *abstraction*, guys!
