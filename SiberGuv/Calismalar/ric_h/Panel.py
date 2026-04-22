from rich.panel import Panel
from rich.console import Console
from rich.table import Table
console = Console()
#* Nmap sonuçları için tablo taslağı
table = Table(title="Nmap Tarama Sonuçları", style="bold cyan")
table.add_column("Port", justify="right", style="magenta")
table.add_column("Servis", style="green")
table.add_column("Versiyon", style="yellow")
table.add_column("Durum", style="bold red")
table.add_row("22", "SSH", "OpenSSH 8.2p1", "Vulnerable") #* 22.port ssh servisi openssh versityonu ve tehlikeli durm
#? Tabloyu panele yerleştirme
console.print(Panel(table, title="[bold white] Sistem analiz paketi[/]", border_style="blue", expand=False))#boyutu kendi ayarlar expand
