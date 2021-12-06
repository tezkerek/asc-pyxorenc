#!/usr/bin/python

import argparse
import string

VALID_KEY_CHARS = string.ascii_letters + string.digits
VALID_DECRYPTION_CHARS = (
    string.ascii_letters + string.digits + string.punctuation + " \n"
)

parser = argparse.ArgumentParser(description="Find the XOR key")
parser.add_argument("input_file")

args = parser.parse_args()

with open(args.input_file, "rb") as input_file:
    enc_bytes = input_file.read()
    enc_len = len(enc_bytes)

    for key_len in range(10, 16):
        key = []

        for key_idx in range(0, key_len):
            # Try every valid character
            for key_byte in VALID_KEY_CHARS:
                # XOR key_byte with every key_len byte in enc_bytes and verify
                # that the result is valid
                for enc_byte_idx in range(key_idx, enc_len, key_len):
                    enc_byte = enc_bytes[enc_byte_idx]
                    dec_byte = chr(enc_byte ^ ord(key_byte))

                    if dec_byte not in VALID_DECRYPTION_CHARS:
                        break
                else:
                    key.append(key_byte)
                    break
        if key:
            print("Possible key", "".join(key), "of length", key_len)
