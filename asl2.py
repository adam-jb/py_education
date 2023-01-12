import asyncio
import logging
from logging.handlers import QueueHandler, QueueListener
import random


# QueueHandler to write to log when queued then pop from it



# QueueListener to listen for changes



# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        value = random.random()
        await asyncio.sleep(value)
        await queue.put(value)
    await queue.put(None)
    print('Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    while True:
        try:
            item = queue.get_nowait()  # get_nowait() is non-blocking version of get()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        if item is None:
            break
        print(f'>got {item}')

    print('Consumer: Done')

# entry point coroutine
async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


asyncio.run(main())
