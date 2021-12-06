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

## *Optimiștii* vs *Robert și Tudor*
Opponent: [trifangrobert/Encrypt-Decrypt-Xor](https://github.com/trifangrobert/Encrypt-Decrypt-Xor)  
Opponent's password: `z7SaQjVrY4RpigO`

#### Knowing the source input
We know that `output = input.txt XOR repeated_key`, and that XOR is
commutative. Therefore, we can XOR `input.txt` and `output` to find the key:

    input.txt XOR output = input.txt XOR (input.txt XOR repeated_key) = repeated_key = z7SaQjVrY4RpigOz7SaQjVrY4RpigOz7SaQjVrY4RpigOz7SaQjVrY4RpigOz7Sa...

The script `xor_files.py` can be used to XOR the input and output and find the key.
