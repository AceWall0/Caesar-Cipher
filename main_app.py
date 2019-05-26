import requests
import json
import hashlib


def main():
    fileName = requestFile('1abaff9bcb0a63706797ae23058898e3f6539f19')
    decodeFile(fileName)


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


def sha1(text: str):
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def requestFile(token):
    """Downloads the json file from the challange with given token and returns the file name."""
    r = requests.get(f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={token}')
    filename = 'answer.json'
    with open(filename, 'w') as f:
        f.write(json.dumps(r.json(), indent=4))
    return filename


def decodeFile(filename):
    """Decodes the ciphered text in the json file from the challange"""
    with open(filename, 'r+') as f:
        data = json.loads(f.read())
        f.seek(0)
        decoded = decode(data['cifrado'], data['numero_casas'])
        data['decifrado'] = decoded
        data["resumo_criptografico"] = sha1(decoded)
        f.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    main()