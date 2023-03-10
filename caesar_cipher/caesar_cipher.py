#!/usr/bin/python3
"""
    Encrypt/Decrypt strings using caesar cipher.
    It can encrypt any string with chracters in range of 32 (SPACE) to 126 (~) in ascii code.
    That is every printable ascii character. If a character is beyond that range, it keep it untouched.

    example:
        $ ./caesar_cipher.py "sample text" -k 8  

    brute-force decryption:
        $ ./caesar_cipher.py '{iuxtm(|m!|' -f

    use negative keys for decrytion with a specific key:
        $ ./caesar_cipher.py '{iuxtm(|m!|' -k -8

"""
import argparse

FIRST_SYMBOLE_ASCII_INDEX = ord(" ")
LAST_SYMBOLE_ASCII_INDEX = ord("~")
INDEX_PADDING = FIRST_SYMBOLE_ASCII_INDEX
SYMBOLS_LENGTH = LAST_SYMBOLE_ASCII_INDEX - FIRST_SYMBOLE_ASCII_INDEX + 1 # [SPACE, ~] -> [32, 126] -> 96 symbols


def encrypt(plaintext: str, key: int):
    ciphertext = ""
    
    for character in plaintext:
        ascii_code = ord(character)

        # If character is out of symboles range, keep it untouched
        if ascii_code > LAST_SYMBOLE_ASCII_INDEX or ascii_code < FIRST_SYMBOLE_ASCII_INDEX:
            ciphertext += character
            continue

        symbol_index = ascii_code - INDEX_PADDING
        new_index = ((symbol_index + key) % SYMBOLS_LENGTH) + INDEX_PADDING
        ciphertext += chr(new_index)

    return ciphertext


def decrypt_brute_force(plaintext: str):
    for key in range(1, SYMBOLS_LENGTH + 1):
        print(f'key #{key}: {encrypt(plaintext, -key)}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Caesar Cipher Enrypt/Decrypt",
        description="Enrypt/Decrypt strings using caesar cipher.",
        usage="caesar_cipher.py teststring -k 2"
    )

    parser.add_argument("string", type=str, help="given string for encryption or brute-force decryption")
    parser.add_argument("-k", "--key", type=int, help="encryption key")
    parser.add_argument("-f", action="store_true", help="brute-force decrypt")

    args = parser.parse_args()
    
    if not (args.key or args.f):
        raise("There most be -f or -k option")
    
    if args.key and args.f:
        raise("-f option and -k option shoudn't be used together")

    if args.f:
        decrypt_brute_force(args.string)
    else:
        print(encrypt(args.string, args.key))
    