"""
Functions to encode, decode and brute-force a ceasar cipher.
"""


def caesar_cipher(input, n, type='encode'):
    """Encode text with a caesar cipher right shift of n."""
    input = input.lower()
    n = n % 26
    if type == 'decode':
        n = -n
    
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc_shift = abc[n:] + abc[:n]
    cipher_map = {}
    for c,c_s in zip(abc, abc_shift):
        cipher_map[c] = c_s
    
    output = ''
    for c in input:
        if c in abc:
            output += cipher_map[c]
        else:
            output += c
    
    return output


def caesar_brute_force(text_encoded):
    """Use brute force to break a caesar cipher."""
    for n in range(26):
        text_decoded = caesar_cipher(text_encoded, n, type='decode')
        print("{}: {}".format(n, text_decoded))


if __name__ == '__main__':
    # Ask for input
    text = input("Text to encode > ")
    n = eval(input("Amount of right shift > "))
    
    # Play with the input
    print("Original text: " + text)
    text_encoded = caesar_cipher(text, n)
    print("Encoded text: " + text_encoded)
    text_decoded = caesar_cipher(text_encoded, n, type='decode')
    print("Decoded encoded text: " + text_decoded)
    caesar_brute_force(text_encoded)

# End
