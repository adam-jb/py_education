

# uvicorn starlette_post:app --reload

# curl -X POST -H "Content-Type: application/json" -d '{"example": "data"}' http://localhost:8000/json


from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse
import asyncio


async def endit(request):
	return JSONResponse('hi')


async def numbers():
    for i in range(3):
        await asyncio.sleep(0.9)
        yield dict(data=i)


async def json_endpoint(request: Request):
    json_data = await request.json()
    generator = numbers()
    return EventSourceResponse(generator)
    #return JSONResponse(content=json_data)


routes = [
    Route("/json", endpoint=json_endpoint, methods=["GET", "POST"]),
    Route("/", endpoint=endit)
]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8121, log_level='info')



