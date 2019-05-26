def encode(text: str, shift: int):
    text = text.lower()
    output = ''
    for char in text:
        code = ord(char) - 97
        if 0 <= code < 26:
            code = (code + shift) % 26
        output += chr(code + 97)

    return output


def decode(text: str, unshift: int):
    return encode(text, -unshift)
