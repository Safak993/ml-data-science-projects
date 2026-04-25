import sys
from rich.console import Console
from rich.panel import Panel
console = Console()
sa = sys.argv[1] #* Liste  olusturuyor python First.py (bir kelime yazı sayı girin)
console.print(sa)
sys.path.insert(0, "/benim/ozel/klasorum") # enbaşa özel birşey ekliyoruz (gerçek klasörede bakar)
console.print(Panel("[bold blue]Pythonun baktığı klasörler🔮[/]", expand=False, border_style="bold blue"))
console.print(f"{sys.path}") #* Python'un baktığı tüm klasörleri ekrana basar
console.print(Panel("[bold blue]Python versiyon🧵[/]", expand=False, border_style="bold blue"))
console.print(f"[bold yellow]{sys.version}[/]")

console.print(Panel("[bold magenta]Kod hangi iletim sisteminde çalşıyor(win32, linux, darwin)🎀[/]", expand=False, border_style="bold magenta")) #* Kodun hangi işletim sisteminde çalıştığını söyler
console.print(f"[bold red]{sys.platform}[/]")
console.print(Panel("[bold red]Bir değişkenin kaç byte kullandığını gösterir🅱[/]", expand=False, border_style="bold red")) #* Bir değişkenin bellekte (RAM) tam olarak kaç byte yer kapladığını söyler.
degisken = "Naberr" #47
console.print(f"[bold yellow]{sys.getsizeof(degisken)}[/]")
