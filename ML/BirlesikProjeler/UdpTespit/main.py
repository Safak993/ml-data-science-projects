from scapy.all import *
import asyncio as io
import time
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from collections import defaultdict
import os
import json
import queue
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
#================================================
#- By Safak993 DDoS Udp saldırılarını engelleme
#- Hazır Data Set
#================================================

df_raw = pd.read_parquet("UDP-training.parquet")
data = {
    'paket'     : df_raw['Total Fwd Packets'],
    'hiz'       : df_raw['Flow Packets/s'],
    'sure'      : df_raw['Flow Duration'],
    'paket_boy' : df_raw['Packet Length Mean'],
    'sonuc'     : df_raw['Label'].apply(lambda x: 0 if x == "Benign" else 1)
}
df = pd.DataFrame(data)
X = df[['paket', 'hiz', 'sure', 'paket_boy']]
y = df['sonuc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train) 


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("-" * 30)
print(f"✅ Model Başarı Oranı: %{accuracy * 100:.2f}")
print("-" * 30)
model = DecisionTreeClassifier()
model.fit(X, y)

ip_gecmisi = defaultdict(list)
kuyruk = queue.Queue()

def paket_isle(paket):
    if IP in paket and UDP in paket:
        kuyruk.put(paket)

# Sniffer sürekli arka planda çalışır
sniffer = AsyncSniffer(iface="\\Device\\NPF_Loopback", filter="udp", prn=paket_isle)
sniffer.start()
saldiri_verileri = df[df['sonuc'] == 1]
print(f"📊 Veri setindeki ortalama saldırı hızı: {saldiri_verileri['hiz'].mean():.2f} paket/s")
async def analiz():
    sayac = 0
    tum_paketler = []
    
    while True:
        while not kuyruk.empty():
            paket = kuyruk.get()
            src_ip = paket[IP].src
            simdi = time.time()
            ip_gecmisi[src_ip].append({"zaman": simdi, "boyut": len(paket)})
            ip_gecmisi[src_ip] = [p for p in ip_gecmisi[src_ip] if simdi - p["zaman"] < 0.1]
            gecmis = ip_gecmisi[src_ip]
            paket_sayisi = len(gecmis)
            if paket_sayisi > 1:
                sure = simdi - gecmis[0]["zaman"]
                sure = max(sure, 0.001) 
                hiz_sn = paket_sayisi / sure # Saniyedeki paket (Ekrana yazdırmak için)
                sure_micro = sure * 1_000_000
                hiz_micro = hiz_sn # Modelin beklediği Flow Packets/s
            else:
                hiz_sn = 0
                sure_micro = 0
                hiz_micro = 0
            # Hesaplanmış boyutu al
            boy = sum(p["boyut"] for p in gecmis) / paket_sayisi
            tahmin = model.predict([[paket_sayisi, hiz_sn, sure_micro, boy]])
            print("="*40)
            durum = "⚠️ DDoS!" if tahmin[0] == 1 else "✅ Normal"
            print(f"{src_ip} | paket:{paket_sayisi} | hız:{hiz_sn:.1f}/s | {durum}")
            print("="*40)

            # JSON'a ekle ama henüz yazma
            tum_paketler.append({
                "kaynak_ip": paket[IP].src,
                "kaynak_port": paket[UDP].sport,
                "hedef_ip": paket[IP].dst,
                "hedef_port": paket[UDP].dport
            })
            sayac += 1

            # Her 100 pakette bir yaz
            if sayac % 100 == 0:
                with open("packets.json", "w") as f:
                    json.dump(tum_paketler, f, indent=4)
                print(f"💾 {sayac} paket kaydedildi")
            if sayac % 100 == 0 and durum =="⚠️ DDoS!":
               with open("ddos_log.json", "w") as f:
                   json.dump(tum_paketler, f, indent=4)
               print(f"🚨 DDoS kaydedildi!")
        await io.sleep(0.001)  

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
#öğrenim ağacı
plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X.columns, class_names=['Normal', 'DDoS'], filled=True)
plt.savefig("diabetes_decision_tree.png", dpi=300, bbox_inches='tight')
plt.show()

if __name__ == "__main__":
    io.run(analiz())
#===================================================================================================================================


#- Eğer biranda ddos! derse çok şaşmayın eğer bir kasıntı yoksa ve birazcık atıp bırakıyosa korkulucak birşey yok
#- İnternetiniz hızlıysa anlık olarak 200 300 udp (fazla bitli) gelebilir bunlar sizin internetinizle alakalı gerçek ddos bu değildir
#- Gerçek DDoS aynı anda 2000 3000 paket zehirler  
#- Arasıra ddos arasıra normal diyorsa buda normal bir durumdur zehirlenme değildir
#- Olabilite durumlar:
#- Her saniye ddos uyarısı geliyorsa
#- 1saniyede 10000 civarı pakey geliyorsa


#- By Safak993/Siber Güvenlik
#==================================================================================================================================
