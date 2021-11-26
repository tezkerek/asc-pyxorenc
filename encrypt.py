import argparse

parser = argparse.ArgumentParser(description="Encrypt a file using XOR")
parser.add_argument("password", type=str, action="store", help="the encryption key")
parser.add_argument("input_file", type=str, action="store", help="the input file")
parser.add_argument(
    "output_file",
    type=str,
    action="store",
    help="the file that will contain the encrypted output",
)

args = parser.parse_args()

key_len = len(args.password)
chunk_size = 1024 // key_len * key_len
repeated_key = chunk_size // key_len * args.password
byte_key = bytes(repeated_key, "utf-8")

with open(args.input_file, "rb") as infile, open(args.output_file, "wb") as outfile:
    in_bytes = infile.read(chunk_size)
    while in_bytes:
        enc_bytes = bytes([b ^ k for b, k in zip(in_bytes, byte_key)])
        outfile.write(enc_bytes)

        in_bytes = infile.read(chunk_size)
