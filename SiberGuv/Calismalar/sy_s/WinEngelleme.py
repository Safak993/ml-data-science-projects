import sys
from rich.console import Console
console = Console()
if sys.platform == "linux":
    console.print(f"[bold red] [!] Windows Kullananlara giriş yasak![/]")
else:
    console.print(f"[bold green] [*] HoşGeldiniz linux kullanıcısı[/]")