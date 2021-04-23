from socket import socket

import asyncio
import websockets


async def test():
    async with websockets.connect('ws://192.168.10.86:8082/try') as websocket:
        await websocket.send("hello")

        response = await websocket.recv()
        print(response)


asyncio.get_event_loop().run_until_complete(test())