from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import cgi

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()
plaintext = form.getvalue("plaintext")
print(plaintext + "from text_des.py")

# BLOCK_SIZE = 32


# def encrypt(text, key):
#     encrypt_des = DES.new(key, DES.MODE_ECB)
#     padded_text = pad(text, BLOCK_SIZE)
#     encrypted_text = encrypt_des.encrypt(padded_text)
#     return encrypted_text


# def decrypt(cipher, key):
#     decrypt_des = DES.new(key, DES.MODE_ECB)
#     decrypted_text = decrypt_des.decrypt(cipher).decode('ascii')
#     # https://developer.mozilla.org/en-US/docs/Glossary/CRLF
#     return decrypted_text


# # harus 8 digit, jadi global variabel
# key = b'QWERTYUI'
# raw = b'plain text uji coba'

# cipher_text = encrypt(raw, key)

# # dekripsi
# replain_text = decrypt(cipher_text, key)

# print(f'{cipher_text}')
# print(replain_text)
