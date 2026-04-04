from scapy.all import *
import asyncio as io
import time
import sys
analiz_bitti = False
tahmin_sonucu = None
baslangic_zamani = 0
async def taramayap():
    global analiz_bitti, baslangic_zamani
    tarama = AsyncSniffer()
    tarama.start()
    await io.sleep(2)
    yakalananlar = tarama.stop()
    analiz_bitti = True
    print(yakalananlar)
    if yakalananlar:
        yakalananlar.summary()
async def animation():
    global analiz_bitti, baslangic_zamani
    karakterler = ["|", "/", "-", "\\"]
    idx = 0
    while not analiz_bitti:
        
        gecen_sure = time.perf_counter() - baslangic_zamani
        sys.stdout.write(f"\r🔍 ANALİZ EDİLİYOR... {karakterler[idx]} [{gecen_sure: .6f} sn]")
        sys.stdout.flush()
        idx = (idx + 1) % len(karakterler)
        await io.sleep(0.05)
async def calistir():
    global baslangic_zamani, analiz_bitti
    baslangic_zamani = time.perf_counter()
    await io.gather(taramayap(), animation())
    bitis_zamani = time.perf_counter()
    toplam_sure = bitis_zamani - baslangic_zamani
    print(f"\n✅ Analiz tamamlandı. Toplam süre: {toplam_sure:.8f} saniye")

if __name__ == "__main__"  :  
    io.run(calistir())