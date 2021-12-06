#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description="XOR two files to find the key")
parser.add_argument("file1")
parser.add_argument("file2")

args = parser.parse_args()

with open(args.file1, "rb") as file1, open(args.file2, "rb") as file2:
    # Read first 30 bytes
    repeated_key = bytes(b1 ^ b2 for (b1, b2) in zip(file1.read(30), file2.read(30)))

    # Try to find the actual key of length 10-15
    for key_len in range(10, 16):
        if repeated_key[:key_len] == repeated_key[key_len : 2 * key_len]:
            print("Key:", repeated_key[:key_len].decode("utf-8"))
            break
    else:
        # Otherwise just print the first 30 bytes
        print("First 30 bytes of key:", repeated_key)
