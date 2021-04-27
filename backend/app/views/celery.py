import time

import websockets
import json


# ACYNC CELERY TASKS
async def send_gls_task(**kwargs):
    async with websockets.connect('ws://192.168.10.86:8082/order_pallet/') as ws:
        await ws.send('Celery Client Connected')
        response = await ws.recv()
        print(response)
        while True:
            await ws.send(json.dumps(f'{kwargs}'))
            request = await ws.recv()
            print(request)
            time.sleep(5)
