# GLS FAKE ENDPOINT
clients = {'1234': [], }


async def gls_fake(request, ws):
    while True:
        data = await ws.recv()
        if data in clients.keys():
            id = data
            messages = clients[id]
            for message in messages:
                await ws.send(message)
            clients[id] = []
        else:
            clients['1234'].append(data)
            await ws.send('Your data has been required')
