import string


# Loop and calculate the shift manually, needs check if uppercase or lowercase : O(n)
def decipher_uppercase(msg, shift):
    results = []
    for letter in msg:
        ascii_val = ord(letter)

        if 'A' <= letter <= 'Z':  # Check if it is uppercase
            shifted = chr(((ascii_val - ord("A") - shift) % 26) + ord("A"))
            results.append(shifted)

    return results


# Lookup Dictionary O(n)
def decipher_lookup(msg, shift):
    letters = string.ascii_uppercase
    shifted_letters = letters[-shift:] + letters[:-shift]
    lookup = dict(zip(letters, shifted_letters))
    return ''.join([lookup[letter] if letter in lookup else letter for letter in msg])


# Built in maketrans() Function O(n)
def decipher_translate(msg, shift):
    letters = string.ascii_uppercase
    shifted_letters = letters[-shift:] + letters[:-shift]
    trans = str.maketrans(letters, shifted_letters)
    return msg.translate(trans)


if __name__ == '__main__':
    expected_result = "LOVETHEDISCIPLINEYOUKNOWANDLETITSUPPORTYOU"
    cyphered = 'ORYHWKHGLVFLSOLQHBRXNQRZDQGOHWLWVXSSRUWBRX'
    current_shift = 3
    marcus = decipher_uppercase(cyphered, current_shift)

    result = ''.join(marcus)
    dict_result = decipher_lookup(cyphered, current_shift)
    translate_result = decipher_translate(cyphered, current_shift)

    assert result == expected_result, f'Error, it was {result}'
    assert dict_result == expected_result, f'Error, it was {dict_result}'
    assert translate_result == expected_result, f'Error, it was {translate_result}'
