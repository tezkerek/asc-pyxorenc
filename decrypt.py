import argparse

CHUNK_SIZE_LIMIT = 4096

parser = argparse.ArgumentParser(description="Decrypt a file using XOR")
parser.add_argument("enc_file", help="the encrypted file")
parser.add_argument("password", help="the decryption key")
parser.add_argument("output_file", help="the decrypted output file")

args = parser.parse_args()

key = bytes(args.password, "utf-8")
key_len = len(key)

# Chunk size will be a multiple of the key length
chunk_size = CHUNK_SIZE_LIMIT // key_len * key_len

with open(args.enc_file, "rb") as enc_file, open(args.output_file, "wb") as dec_file:
    enc_bytes = enc_file.read(chunk_size)
    while enc_bytes:
        dec_bytes = bytes(b ^ key[i % key_len] for (i, b) in enumerate(enc_bytes))
        dec_file.write(dec_bytes)

        enc_bytes = enc_file.read(chunk_size)
