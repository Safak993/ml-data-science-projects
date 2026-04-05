#Belirli paket türünü yakalama
from scapy.all import *
import asyncio as io
import sys
import time
import json
analiz_bitti = False
tahmin_sonucu = None
baslangic_zamani = 0
async def tara():
    global analiz_bitti, baslangic_zamani
    s = AsyncSniffer(filter="tcp", count=800)#800 tcp paketi yakalıcak
    s.start()
    while s.running:
        await io.sleep(0.1)
    yakalanan = s.results or []
    analiz_bitti = True
    paket_listesi = []
    for paket in yakalanan:
        print("Tarama bitti. Sonuçlar:\n\n")
        print("="*50)
        print("\n 📦Paket Türü: TCP\n\n")
        print("Kaynak: \n")
        print("="*50)
        print(f"Kaynak IP: {paket[IP].src}")
        print(f"Kaynak Port: {paket[TCP].sport}")
        print("="*50)
        print("\n Hedef: \n")
        print("="*50)
        print(f"Hedef IP: {paket[IP].dst}")
        print(f"Hedef Port: {paket[TCP].dport}")
        print("="*50)
        if IP in paket and TCP in paket:
            paket_listesi.append({
                "kaynak_ip": paket[IP].src,
                "kaynak_port": paket[TCP].sport,
                "hedef_ip": paket[IP].dst,
                "hedef_port": paket[TCP].dport,
            })
    with open("paketler.json", "w") as f:
        json.dump(paket_listesi, f, indent=4)
    print(f"\n💾 {len(paket_listesi)} paket 'paketler.json' dosyasına kaydedildi.")
async def animation():
    karakterler = ["|", "/", "-", "\\"]
    idx = 0
    while not analiz_bitti:
        
        gecen_sure = time.perf_counter() - baslangic_zamani
        sys.stdout.write(f"\r🔍 ANALİZ EDİLİYOR... {karakterler[idx]} [{gecen_sure: .6f} sn]")
        sys.stdout.flush()
        idx = (idx + 1) % len(karakterler)
        await io.sleep(0.05)
async def calis():
    global baslangic_zamani, analiz_bitti
    baslangic_zamani = time.perf_counter()
    await io.gather(tara(), animation())
    bitis_zamani = time.perf_counter()
    toplam_sure = bitis_zamani - baslangic_zamani
    print(f"\n✅ Analiz tamamlandı. Toplam süre: {toplam_sure:.8f} saniye")
    
if __name__ == "__main__":
    io.run(calis())
#===================
#By Safak993
#===================