import logging


letters = [i for i in range(65, 91)] + [i for i in range(97, 123)]

# Function for text encryprion
def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if ord(char) not in letters:
            result += char
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


# Function for text decryption
def decrypt(text, shift):
    result = ''

    for i in range(len(text)):
        char = text[i]
        if ord(char) not in letters:
            result += char
        elif char.isupper():
            result += chr((ord(char) - shift + 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift + 85) % 26 + 97)

    return result


# Main logic of the program
def main():
    format = "%(asctime)s - %(message)s"
    logging.basicConfig(filename="cipher.log", level=logging.INFO, format=format)

    state = True
    print("Hello there! \n")
    logging.info('Program started')

    while state:
        # Mode selection
        mode = str(input("Type an integer to choose a mode. \n1. Encrypt text \n2. Decrypt text \n3. Exit \n"))
        logging.info(f'User chose mode {mode}')

        if mode == '1':
            text = str(input("Enter some text (only latin alphabet): "))
            logging.info(f'User entered text: {text}')
            try:
                shift = int(input("Enter a cipher shift: "))
                logging.info(f"User entered shift {shift}")
                print(f'Encrypted text: {encrypt(text, shift)} \n')
                logging.info(f'The encrypted text: {encrypt(text, shift)}')
            except ValueError:
                print("It is not an integer. Let's try again. \n")
                logging.info(f'User entered wrong shift value')

        elif mode == '2':
            text = str(input("Enter encrypted text (only latin alphabet): "))
            logging.info(f'User entered text: {text}')
            try:
                shift = int(input("Enter a cipher shift: "))
                logging.info(f"User entered shift {shift}")
                print(f'Decrypted text: {decrypt(text, shift)} \n')
                logging.info(f'The decrypted text: {decrypt(text, shift)}')
            except ValueError:
                print("It is not an integer. Let's try again. \n")
                logging.info(f'User entered wrong shift value')

        elif mode == '3':
            print('Goodbye!')
            logging.info("Program ended")
            state = False

        else:
            # Error handling
            logging.info("User entered incorrect value")
            print("Incorrect input. Please, try again \n")


if __name__ == "__main__":
    main()