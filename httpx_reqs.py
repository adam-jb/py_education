import asyncio
from httpx import AsyncClient
from time import time

async def main():
    urls = [
        "https://www.bbc.co.uk" for _ in range(10)
    ]
    async with AsyncClient() as client:
        t1 = time()
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            pass
            #print(response.status_code)
            #print(response.text)
        t2 = time()
        print(t2 - t1)

asyncio.run(main())
