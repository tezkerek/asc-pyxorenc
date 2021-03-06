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
characters. The script `brute_force_key.py` can find the key by brute force in
reasonable time.

* For every possible key length `l = 10..16`:
    * Initialize an empty array of byte arrays `K`, where `K[i]` is an array of
      valid key bytes on position `i` in the key.
    * For every position `i = 0..l` in the key:
        * Choose a valid key char `c` and XOR every byte in the input on
          position `i + nl` with `c`.
        * If all of the XOR results are valid chars, add `c` to `K[i]`, otherwise go to
          the next potential key char.
        * If no valid key char was found for position `i`, skip to the next
          possible key length `l`.
    * Compute the Cartesian product of `K`'s byte array items to obtain a list
      of possible keys of length `l`.
