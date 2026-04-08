import requests as req
cevap = req.get('https://api.github.com/users/Safak993')
print("="*40)
print(cevap.status_code)
print("="*40)
print(cevap.text)
print("="*40)