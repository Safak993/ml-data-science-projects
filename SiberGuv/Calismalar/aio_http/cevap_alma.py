import asyncio
import aiohttp
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

async def siteyi_kontrol_et(session, url):
    """Tek bir siteyi tarar ve tablosunu basar."""
    try:
        # 'oturum' yerine 'cevap' (response) ismini kullandık
        async with session.get(url, timeout=5) as cevap:
            table = Table(title=f"\n[bold blue]{url}[/bold blue] Analiz Sonuçları", show_lines=True)
            table.add_column("Parametre", style="cyan", no_wrap=True)
            table.add_column("Değer", style="magenta")

            headers = cevap.headers
            kritik_basliklar = [
                'Server', 'Content-Type', 'Content-Encoding', 
                'X-Frame-Options', 'Content-Security-Policy'
            ]

            for key in kritik_basliklar:
                val = headers.get(key, "[red]Eksik (Güvenlik Riski!)[/red]")
                if len(val) > 80: val = val[:77] + "..."
                table.add_row(key, val)

            console.print(table)
            console.print(f"[bold yellow][!][/bold yellow] Toplam Çerez Sayısı: [bold]{len(cevap.cookies)}[/bold]")
            
    except Exception as e:
        console.print(f"[bold red]Hata ({url}):[/bold red] {e}")

async def main():
    target_list = [
        "https://github.com",
        "https://google.com",
        "https://python.org"
    ]
    
    console.print(Panel("[bold green]HTTP Header Analizörü v1.1[/bold green]\n[dim]Asenkron Mod Aktif[/dim]"))

    # Tek bir oturum üzerinden tüm isteklere dağılıyoruz (Performans için)
    async with aiohttp.ClientSession() as session:
        tasks = [siteyi_kontrol_et(session, url) for url in target_list]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())