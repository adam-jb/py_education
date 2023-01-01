import asyncio
import time
import requests



### attempting to run concurrent requests to a url: seems to run synchronously atm
async def get_req_i(url, i):
    print(i)
    return requests.get(url).text


awaitables_list = [get_req_i('http://www.google.com', i) for i in range(100)]

async def main():
    # L = 
    L = asyncio.gather(
        *awaitables_list
    )
    await L
    print(L)
asyncio.run(main())
print('done')




async def get_req(url):
    return requests.get(url).text

# make 100 async queries and store results in a dict
g_result = {}
async def main():
    global g_result
    tasks = []
    for i in range(100):
        t = asyncio.create_task(get_req('http://www.google.com'))
        await t
        print(asyncio.get_running_loop())
        g_result[i] = t.result()
asyncio.run(main())
print(f'got google with len {len(g_result)}')

#### end of attempts





# makes multiple subprocesses to run in parallel
async def main():
    await asyncio.gather(
        await asyncio.create_subprocess_shell('ls -la'),
        await asyncio.create_subprocess_shell('sleep 1; echo "hello"')
    )
asyncio.run(main())



# this gives a warning as test() is never run as it is never awaited
async def test():
    print("never scheduled")
async def main():
    test()
asyncio.run(main())


# this time it gets run
async def main():
    await test()
asyncio.run(main())



async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


## this runs synchronously
async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


## this runs asynchronously, as it uses the asyncio.create_task() wrapper
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


# this is same as above (async), using asyncio.TaskGroup() context manager to be simpler
# asyncio.TaskGroup() was added in python3.11
"""
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The wait is implicit when the context manager exits.
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
"""


# asyncio.gather() schedules coroutines concurrently
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())





















