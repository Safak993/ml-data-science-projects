from Crypto.Cipher import AES
# 16 byte anahtar ve veri
cipher = AES.new(b'16byte_anahtar__', AES.MODE_EAX)
sifreli = cipher.encrypt(b"gizli mesaj")
print(sifreli.hex())