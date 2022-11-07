import base64
import hashlib
from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'SeguridadInforma'

# Encriptar
def encrypt(text_to_cipher):
    text_to_cipher = text_to_cipher.encode('ascii')
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=key)
    return b64encode(cipher.encrypt(pad(text_to_cipher, AES.block_size))).decode('ascii')

# Desencriptar
def decrypt(text_to_decipher):
    decipher = AES.new(key=key, mode=AES.MODE_CBC, iv=key)
    text = b64decode(text_to_decipher)
    return unpad(decipher.decrypt(text), AES.block_size)

decrypt(b'm8Q9fsGqEfZDAih7F76few==') # traducimos (CyberChef) "9bc43d7ec1aa11f64302287b17be9f7b" de Hex a Base64 porque el algoritmo trabaja en esa base
