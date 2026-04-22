import json
# 1. Örnek bir veri (mmap çıktısı gibi düşünelim)
data = {
    "ip": "192.168.1.1", #? Gerçek bir hedef yok locali ip
    "status": "up",
    "ports": [22, 80, 443]
}
with open("First.json", "w") as js:
    js.write(json.dumps(data, indent=4)) # Dosyaya atıyoruz