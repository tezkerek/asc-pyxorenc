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
Opponent:
[trifangrobert/Encrypt-Decrypt-Xor](https://github.com/trifangrobert/Encrypt-Decrypt-Xor)  
Opponent's password: `z7SaQjVrY4RpigO`

#### Knowing the source input
We know that `output = input.txt XOR repeated_key`, and that XOR is associative
and commutative. Therefore, we can XOR `input.txt` and `output` to find the
repeated key:

    input.txt XOR output = input.txt XOR (input.txt XOR repeated_key) = repeated_key = z7SaQjVrY4RpigOz7SaQjVrY4RpigOz7SaQjVrY4RpigOz7SaQjVrY4RpigOz7Sa...

The script `find_key_from_input.py` can be used to XOR the input and output and find the key.

#### Knowing only the output
We know that the key is short (10-15) and that it contains only alphanumeric
characters. The script `crack.py` can find the key by brute force in reasonable time.

For every possible key length `l = 10..16`, initialize an empty byte array `K`.
For every position `i = 0..l` in the key, choose a valid key char `c` and XOR
every byte in the input on position `i + nl` with `c`. If all of the XOR
results are valid chars, add `c` to `K`, otherwise go to the next potential key
char. When `K` has been filled or we have run out of valid key chars, print `K`
if it is not empty.
