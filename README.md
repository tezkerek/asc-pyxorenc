# Python XOR encryption tool

Usage: `python xor.py <password> <input_file> <output_file>`

Run `python xor.py -h` for help.

## Example
Encrypt `input.txt`:

```bash
$ python xor.py my_password input.txt output
```

Decrypt `output`:

```bash
$ python xor.py my_password output decrypted.txt
```

Verify that the decryption worked:

```bash
$ cmp decrypted.txt input.txt && echo "Files are identical" || echo "Files are different"
```
