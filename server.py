#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve

def test(m):
    return("Input recieved!:", m)

async def echo(websocket):
    async for message in websocket:
        await websocket.send(test(message))

async def main():
    async with serve(echo, "https://server-py-cronos72-dev.apps.sandbox-m3.1530.p1.openshiftapps.com", 8080):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())