def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += char
        elif (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


def decrypt(text, shift):
    result = ''

    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += char
        elif (char.isupper()):
            result += chr((ord(char) - shift + 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift + 85) % 26 + 97)

    return result
