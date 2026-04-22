import time
from rich.live import Live
from rich.table import Table
#! Bu kod öğrenim amaçlıdır içinde gerçek bruteforce bruteforce bulunmaz; bulunsa bile eğitim amaçlıdır.
def tablo_Olustur(current_attempt, status):
    table = Table(title="Brute-Force Durumu")
    table.add_column("Hedef", style="cyan")
    table.add_column("Deneme", style="magenta")
    table.add_column("Durum", style="green" if "Success" in status else "red")
    table.add_row("192.168.1.50", current_attempt, status) #? gerçek bir hedef yok local ip
    
    return table
#* Tableyi canlı yapan o sistem
with Live(tablo_Olustur("admin", "Deneniyor..."), refresh_per_second=4) as live:
    for password in ["123456", "password", "admin123"]:
        time.sleep(1)
        live.update(tablo_Olustur(password, "Hatalı Şifre!"))
    time.sleep(1)
    live.update(tablo_Olustur("admin123", "Success! Found!"))