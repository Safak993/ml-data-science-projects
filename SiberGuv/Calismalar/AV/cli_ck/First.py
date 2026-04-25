import click
from rich.console import Console
#!  Hoşgeldiniz buy projelerin içinde rich,click pywin32 hashlib tarzı AV kütüphaneleri bulunacak iyi günler:)
console = Console()
@click.command()
@click.option('--isim', help='Selamlanacak kişinin adı')
def selam(isim):
    console.print(f"[bold green]Selam! {isim} bu benim ilk click Çalışmam![/bold green]")
    console.print("[bold yellow]Yardım için First.py --help[/bold yellow]")
if __name__ == "__main__":
    selam()