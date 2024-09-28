#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve

def test(m):
    return("Input recieved!:", m)

async def echo(websocket):
    async for message in websocket:
        await websocket.send(test(message))

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())