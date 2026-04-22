import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Başlangıç verisi
veri = {
    "ip": "192.168.1.10",
    "data": {
        "Portlar": [21, 22, 80],
        "Servisler": ["ftp", "ssh", "http"]
    }
}

def Tabloyu_Goster():
    console.clear()
    
    table = Table(title="Nmap Simulator")
    table.add_column("IP", style="bold white")
    table.add_column("Portlar", style="magenta")
    table.add_column("Servisler", style="bold blue")

    # Listeleri okunabilir stringlere çeviriyoruz
    portlar_str = ", ".join(map(str, veri["data"]["Portlar"]))
    servisler_str = ", ".join(veri["data"]["Servisler"])
    
    table.add_row(veri["ip"], portlar_str, servisler_str)
    
    # Tabloyu bir panel içinde basıyoruz
    console.print(Panel(table, border_style="blue", expand=False))

# Ana döngü
while True:
    Tabloyu_Goster()
    
    try:
        # Kullanıcıdan yeni port al
        girdi = console.input("[bold yellow]\nEklemek istediğin Port (Çıkış için 'q'): [/bold yellow]")
        
        if girdi.lower() == 'q':
            break
            
        yeni_port = int(girdi)
        
        # 1. Veriyi güncelle (Bellekte)
        veri["data"]["Portlar"].append(yeni_port)
        
        # 2. JSON dosyasına kaydet (Yönetim)
        with open("yonetim.json", "w") as js:
            json.dump(veri, js, indent=4)
            
    except ValueError:
        console.print("[red]Hata: Lütfen geçerli bir port numarası gir![/red]")
        import time
        time.sleep(1) # Hatayı görmen için kısa bir bekleme
    except KeyboardInterrupt:
        break

console.print("[bold green]\nSimülasyon sonlandırıldı. Veriler 'yonetim.json' dosyasına kaydedildi.[/bold green]")