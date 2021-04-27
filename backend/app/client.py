import time

import asyncio
import websockets


async def test():
    async with websockets.connect('ws://192.168.10.86:8082/order_pallet/') as ws:
        await ws.send("Client connected")
        response = await ws.recv()
        print(response)
        while True:
            await ws.send('1234')
            response = await ws.recv()
            print(response)
            time.sleep(5)

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(test())
asyncio.get_event_loop().run_forever()
