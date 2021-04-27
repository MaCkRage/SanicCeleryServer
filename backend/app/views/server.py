# GLS FAKE ENDPOINT
import json

clients = {'1234': ['No data to responce'], }


async def gls_fake(request, ws):

    client = await ws.recv()
    print('FIRST CONNECTION')
    await ws.send('Server connected')
    print('CLIENT MESSAGE:', client)
    while True:
        data = await ws.recv()
        print('CLIENT MESSAGE:', data)
        if data in clients.keys():
            id = data
            messages = clients[id]
            if messages[0]:
                await ws.send(messages[0])
                clients[id] = ['No data to responce']
            else:
                await ws.send('No data to responce')
            clients[id] = ['No data to responce']
        else:
            clients['1234'].clear()
            clients['1234'].append(json.loads(data))
            await ws.send('Your data has been required')
