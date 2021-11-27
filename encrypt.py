import argparse

CHUNK_SIZE_LIMIT = 4096

parser = argparse.ArgumentParser(description="Encrypt a file using XOR")
parser.add_argument("password", help="the encryption key")
parser.add_argument("input_file", help="the file to encrypt")
parser.add_argument("output_file", help="the encrypted output file")

args = parser.parse_args()

key = bytes(args.password, "utf-8")
key_len = len(key)

# Chunk size will be a multiple of the key length
chunk_size = CHUNK_SIZE_LIMIT // key_len * key_len

with open(args.input_file, "rb") as in_file, open(args.output_file, "wb") as out_file:
    input_bytes = in_file.read(chunk_size)
    while input_bytes:
        enc_bytes = bytes(b ^ key[i % key_len] for (i, b) in enumerate(input_bytes))
        out_file.write(enc_bytes)

        input_bytes = in_file.read(chunk_size)
