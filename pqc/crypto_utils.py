import base64
import os

def generate_keys():
    public_key = os.urandom(32)  
    private_key = os.urandom(32)  
    return public_key, private_key

def encrypt_message(public_key, message):
    
    encoded_message = base64.b64encode(message)  
    return encoded_message

def decrypt_message(private_key, ciphertext):
    
    decoded_message = base64.b64decode(ciphertext)
    return decoded_message
