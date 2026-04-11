from rich.prompt import Prompt, IntPrompt
from rich.console import Console
from rich.table import Table
import json

console = Console()


Ad = Prompt.ask("[bold cyan]Kullanıcı adını gir[/bold cyan]\n[bold red](Kullanıcı):->[/bold red]")
Yas = IntPrompt.ask(f"[bold cyan]Yaşını gir[/bold cyan]\n[bold red]({Ad}):->[/bold red]")

style = "bold red" if Yas > 18 else "bold blue"
table = Table(title="\n[bold cyan]Kullanıcı Bilgileri[/]", show_header=True, header_style="bold green", show_lines=True)

table.add_column("Parametre", style="bold yellow", justify="center")
table.add_column("Değer", style=style, no_wrap=True, justify="center")

# Satırları ekle
table.add_row("Ad", Ad)
table.add_row("Yaş", str(Yas))

console.print("\n", table)

# 3. JSON Kaydetme 
data = {
    "kullanici_bilgileri": {
        "ad": Ad,
        "yas": Yas
    }
}

try:
    with open("data.json", "w", encoding="utf-8") as f:
        
        json.dump(data, f, ensure_ascii=False, indent=4)
    console.print("[green][+] Veriler 'data.json' dosyasına kaydedildi.[/green]")
except Exception as e:
    console.print(f"[red][!] Dosya yazma hatası: {e}[/red]")