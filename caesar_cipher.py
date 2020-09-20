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


def main():
    state = True
    print("Hello there! \n")

    while state:
        mode = str(input("Type an integer to choose a mode. \n1. Encrypt text \n2. Decrypt text \n3. Exit \n"))

        if mode == '1':
            text = str(input("Enter some text (only latin alphabet): "))
            shift = int(input("Enter a cipher shift: "))
            print(f'Encrypted text: {encrypt(text, shift)} \n')

        elif mode == '2':
            text = str(input("Enter encrypted text (only latin alphabet): "))
            shift = int(input("Enter a cipher shift: "))
            print(f'Decrypted text: {decrypt(text, shift)} \n')

        elif mode == '3':
            print('Goodbye!')
            state = False

        else:
            print("Incorrect input. Please, try again \n")


if __name__ == "__main__":
    main()