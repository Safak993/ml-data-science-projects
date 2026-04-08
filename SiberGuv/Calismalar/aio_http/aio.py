import aiohttp, asyncio
async def go():
    async with aiohttp.ClientSession() as s:
        async with s.get('https://api.ipify.org') as r:
            print(f"IP Adresin: {await r.text()}")

asyncio.run(go())