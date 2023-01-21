
# uvicorn sse_starlette_requests:app --reload

import asyncio
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse
from starlette.requests import Request


# EventSourceResponse implements SSE protocol: 
async def numbers():
    for i in range(3):
        await asyncio.sleep(0.9)
        yield dict(data=i)

async def sse(request):
    generator = numbers()    #generator is an async generator object
    print(type(generator))
    rj = await request.json()
    print(f'request: {rj}')
    return EventSourceResponse(generator)

routes = [
    Route("/", endpoint=sse)
]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8111, log_level='info')

