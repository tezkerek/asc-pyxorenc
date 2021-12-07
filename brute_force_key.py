#!/usr/bin/python

import argparse
import string
import itertools

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
        is_valid_length = True
        key_bytes = []

        for key_idx in range(0, key_len):
            key_chars_at_idx = []

            # Find every valid key character for index key_idx
            for key_byte in VALID_KEY_CHARS:
                # XOR key_byte with every key_len byte in enc_bytes and verify
                # that the result is valid
                for enc_byte_idx in range(key_idx, enc_len, key_len):
                    enc_byte = enc_bytes[enc_byte_idx]
                    dec_byte = chr(enc_byte ^ ord(key_byte))

                    if dec_byte not in VALID_DECRYPTION_CHARS:
                        break
                else:
                    key_chars_at_idx.append(key_byte)

            if key_chars_at_idx:
                key_bytes.append(key_chars_at_idx)
            else:
                # There are no valid keys with length key_len
                break

        if key_bytes:
            for key in itertools.product(*key_bytes):
                print(f"Possible key of length {key_len}:", "".join(key))
