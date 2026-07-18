def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== Caesar Cipher Program =====")

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter shift value: "))
        encrypted_text = encrypt(message, shift)
        print("Encrypted Message:", encrypted_text)

    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter shift value: "))
        decrypted_text = decrypt(message, shift)
        print("Decrypted Message:", decrypted_text)

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
