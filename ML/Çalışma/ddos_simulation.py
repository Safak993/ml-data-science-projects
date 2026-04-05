
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import sys
import time
import threading
data = {
    'paket_boyutu': [64, 128, 1500, 1500, 64, 1500, 1500, 512, 92, 130],
    'hiz_ms':       [100, 200, 1, 2, 150, 1, 3, 50, 13, 22],
    'port':         [80, 443, 80, 80, 443, 22, 21, 80, 27, 12],
    'sonuc':        [0, 0, 1, 1, 0, 1, 1, 0, 0, 0] # 0: Normal, 1: Saldırı
}

df = pd.DataFrame(data)
X = df[['paket_boyutu', 'hiz_ms', 'port']]
y = df['sonuc']

# Modeli eğitiyoruz
model = DecisionTreeClassifier()
model.fit(X, y)
print()


yeni_paket = pd.DataFrame([[152, 10, 82132130]], columns=['paket_boyutu', 'hiz_ms', 'port'])
print("\n" + "="*70)
print("     🌐 CANLI DDoS ANALİZ SİSTEMİ 🌐")
print("="*70 + "\n")
#-------------------------------
analiz_bitti = False
tahmin_sonucu = None
baslangic_zamani = 0
def animation():
    karakterler = ["|", "/", "-", "\\"]
    idx = 0
    while not analiz_bitti:
        gecen_sure = time.perf_counter() - baslangic_zamani
        sys.stdout.write(f"\r🔍 ANALİZ EDİLİYOR... {karakterler[idx]} [{gecen_sure: .6f} sn]")
        sys.stdout.flush()
        idx = (idx + 1) % len(karakterler)
        time.sleep(0.05)
#-------------------------------
#animasyonu farklı threade verdik işlemi durdurmasın diye
baslangic_zamani = time.perf_counter()
anim_thread = threading.Thread(target=animation)
anim_thread.start()
time.sleep(1)
tahmin = model.predict(yeni_paket)

analiz_bitti = True
bitis_zamani = time.perf_counter()

anim_thread.join()

toplam_sure = bitis_zamani - baslangic_zamani

print(f"\n✅ Analiz tamamlandı. Toplam süre: {toplam_sure:.8f} saniye.\n")

print("\n" + "="*50)
print(f"📊PAKET VERİSİ:")
print(f"     📏Boyut: {yeni_paket.iloc[0]['paket_boyutu']}")
print(f"     ⏱️  Hız:    {yeni_paket.iloc[0]['hiz_ms']} ms")
print("=" * 50)
print(f"🔮 MODEL KARARI:")
if tahmin[0] == 1:
    print("⚠️ UYARI: Şüpheli DDoS trafiği tespit edildi!")
else:
    print("✅ Trafik normal görünüyor.")
