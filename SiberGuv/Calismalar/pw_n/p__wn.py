from pwn import *
io = remote('hedef-site.com', 1337) # Bağlan
io.sendline(b'pwn_geliyor') # Veri gönder
io.interactive() # Kontrolü bana ver (Shell gibi kullan)