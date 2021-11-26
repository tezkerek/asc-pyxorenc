import argparse

parser = argparse.ArgumentParser(description='Decrypt a file using XOR')
parser.add_argument('encrypted_file', type=str, action='store', help='the encrypted file')
parser.add_argument('password', type=str, action='store', help='the decryption key')
parser.add_argument('output_file', type=str, action='store', help='the file that will contain the decrypted output')

args = parser.parse_args()

key_len = len(args.password)
chunk_size = 1024 // key_len * key_len
repeated_key = chunk_size // key_len * args.password
byte_key = bytes(repeated_key, "utf-8")

with open(args.encrypted_file, "rb") as encfile, open(args.output_file, "wb") as decfile:
    enc_bytes = encfile.read(chunk_size)
    while enc_bytes:
        dec_bytes = bytes([b ^ k for
            b, k in zip(enc_bytes, byte_key)])
        decfile.write(dec_bytes)

        enc_bytes = encfile.read(chunk_size)
