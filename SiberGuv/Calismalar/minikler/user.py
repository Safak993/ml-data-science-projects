import requests as req
cevap = req.get('https://api.github.com/users/Safak993')
veri = cevap.json()
print(veri.get('login'))
print(veri['public_repos'])