def encrypt(text: str):
    text = text.lower()

    output = ''
    for char in text:
        code = ord(char) - 97
        if 0 <= code < 26:
            code = (code + 3) % 26
        output += chr(code + 97)

    return output


print(encrypt('abc - - xyz'))