def caesar_cipher(text, shift, decrypt=False):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + shift) % 26 if not decrypt else (ord(char) - base - shift) % 26
            result += chr(base + offset)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").upper()
        if choice not in ['E', 'D']:
            print("Please choose either 'E' or 'D'.")
            continue
        
        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Shift value must be an integer.")
            continue
        
        if choice == 'E':
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher(message, shift, decrypt=True)
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to encrypt/decrypt another message? (Y/N) ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
