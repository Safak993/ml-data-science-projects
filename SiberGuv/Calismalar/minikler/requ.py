import requests as req
import re

url = 'https://www.youtube.com/@metecetin8683'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    cevap = req.get(url, headers=headers)
    html_icerik = cevap.text

    email_deseni = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    mailler = re.findall(email_deseni, html_icerik)

    print("="*40)
    if mailler:
        print("Bulunan E-postalar:")
        for mail in set(mailler): 
            print(f"- {mail}")
    else:
        print("Kaynak kodda açık bir e-posta adresi bulunamadı.")
    print("="*40)

except Exception as e:
    print(f"Hata oluştu: {e}")