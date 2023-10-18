def caesar_cipher(s, k):
    result = []
    for char in s:
        ascii_val = ord(char)
        if 'a' <= char <= 'z':  # Lowercase letters
            result.append(chr((ascii_val - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':  # Uppercase letters
            result.append(chr((ascii_val - ord('A') + k) % 26 + ord('A')))
        else:  # Non-alphabet characters
            result.append(char)
    return ''.join(result)


if __name__ == '__main__':
    marcus = caesar_cipher('LOVETHEDISCIPLINEYOUKNOWANDLETITSUPPORTYOU', 3)
    assert marcus == 'ORYHWKHGLVFLSOLQHBRXNQRZDQGOHWLWVXSSRUWBRX', f'Error, it was {marcus}'
