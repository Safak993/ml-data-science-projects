import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import sys
import time
import threading
data = {
    'paket': [28, 50, 3168, 9999, 6666],
    'hiz' : [7, 5, 2, 3, 1],
    'port': [80, 443, 80, 80, 80],
    'sonuc': [0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[['paket', 'hiz', 'port']]
y = df['sonuc']
model = DecisionTreeClassifier()
model.fit(X, y)
print()

sendpacket = pd.DataFrame([[60, 5, 80]], columns=['paket', 'hiz', 'port'])
tahmin = model.predict(sendpacket)

if tahmin[0] == 1:
    print("Uyarıı")
else:
    print("sakin")