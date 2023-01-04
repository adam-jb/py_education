import os
import asyncio
import aiohttp  
import aiofiles  

def download_files_from_report(urls, FILES_PATH):
    os.makedirs(FILES_PATH, exist_ok=True)   # make directory if it doesn't exist
    sema = asyncio.BoundedSemaphore(5)

    async def fetch_file(url):
        fname = url.split("/")[-1]
        # aiohttp.ClientSession used for making http requests
        async with sema, aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                assert resp.status == 200
                data = await resp.read()

        # save file asynchronously with aiofiles
        async with aiofiles.open(
            os.path.join(FILES_PATH, fname), "wb"
        ) as outfile:
            await outfile.write(data)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(fetch_file(url)) for url in urls]
        
    #loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    
urls = ['https://tools.learningcontainer.com/sample-json.json',
        'https://tools.learningcontainer.com/sample-json.json']

download_files_from_report(urls, "tmpfiles/")
print('done')