def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        # Check if character is uppercase
        if char.isupper():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += encrypted_char
        # Check if character is lowercase
        elif char.islower():
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += encrypted_char
        else:
            # Leave spaces, numbers, and punctuation unchanged
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        # Check if character is uppercase
        if char.isupper():
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            plaintext += decrypted_char
        # Check if character is lowercase
        elif char.islower():
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            plaintext += decrypted_char
        else:
            # Leave spaces, numbers, and punctuation unchanged
            plaintext += char
    return plaintext

def main():
    print("--- DecodeLabs: Cryptographic Engine (Caesar Cipher) ---")
    
    # Input Phase
    user_text = input("Enter the text to encrypt: ")
    try:
        shift_key = int(input("Enter the shift key (integer): "))
    except ValueError:
        print("Invalid shift key. Defaulting to shift of 3.")
        shift_key = 3

    # Process Phase (Encryption)
    encrypted_text = caesar_encrypt(user_text, shift_key)
    
    # Process Phase (Decryption Validation)
    decrypted_text = caesar_decrypt(encrypted_text, shift_key)

    # Output Phase
    print("\n[+] Results:")
    print(f"Original Plaintext : {user_text}")
    print(f"Encrypted Ciphertext: {encrypted_text}")
    print(f"Decrypted Text     : {decrypted_text}")

if __name__ == "__main__":
    main()
