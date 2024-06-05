def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? (E/D): ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice, please enter E or D.")
            continue
        message = input("Enter your message: ")
        while True:
            try:
                shift = int(input("Enter the shift value: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid integer for the shift value.")
        if choice == 'E':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'D':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        continue_choice = input("Do you want to encrypt/decrypt another message? (Y/N): ").upper()
        if continue_choice != 'Y':
            break

if __name__ == "__main__":
    main()
