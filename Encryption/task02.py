def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

# Exemple d'utilisation
plain_text = "HelloWorld"
key = "KEY"
encrypted_text = encrypt_vigenere(plain_text, key)
print("Texte chiffré:", encrypted_text)

decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Texte déchiffré:", decrypted_text)
