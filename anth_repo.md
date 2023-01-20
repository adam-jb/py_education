

uvicorn is an async web server and can host an async fastAPI and starlette:
```
uvicorn main:app --reload


## the app
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    await asyncio.sleep(1)
    return {"item_id": item_id}
```

Q: what are Server-Sent Events?
A: server push technology enabling a client to receive automatic updates from a server via an HTTP connection


The below implements SSE to yield results from a generator in a stream:
```
# uvicorn sse:app --reload
import asyncio
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse

# EventSourceResponse implements SSE protocol: 
async def numbers():
    for i in range(3):
        await asyncio.sleep(0.9)
        yield dict(data=i)

async def sse(request):
    generator = numbers()    #generator is an async generator object
    print(type(generator))
    return EventSourceResponse(generator)

routes = [
    Route("/", endpoint=sse)
]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8111, log_level='info')

```












