import random
import string

def generate_substitution_key():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    
    return {original: shuffled for original, shuffled in zip(alphabet, shuffled_alphabet)}

def encrypt_message(message, key):
    encrypted_message = ""
    
    for char in message.lower():
        if char in key:
            encrypted_message += key[char]
        else:
            encrypted_message += char  # Mantém espaços, números e pontuação
    
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Inverter a chave para mapear de volta ao original
    reversed_key = {v: k for k, v in key.items()}
    
    decrypted_message = ""
    for char in encrypted_message:
        if char in reversed_key:
            decrypted_message += reversed_key[char]
        else:
            decrypted_message += char  # Mantém espaços, números e pontuação

    return decrypted_message

# Gerar chave de substituição
key = generate_substitution_key()

# Testando criptografia
test_message = "hello world"
encrypted = encrypt_message(test_message, key)
print("Substitution Key:", key)
print("Encrypted Message:", encrypted)

# Testando descriptografia
decrypted = decrypt_message(encrypted, key)
print("Decrypted Message:", decrypted)
