# GLS FAKE ENDPOINT
clients = {'1234': ['No data to responce'], }


async def gls_fake(request, ws):
    client = await ws.recv()
    print('ПЕРВОЕ ПОДКЛЮЧЕНИЕ', client)
    await ws.send('Server connected')
    while True:
        data = await ws.recv()
        if data in clients.keys():
            id = data
            messages = clients[id]
            if messages[1]:
                await ws.send(messages[1])
            else:
                await ws.send('No data to responce')
            clients[id] = ['No data to responce']
        else:
            clients['1234'].clear()
            clients['1234'].append(data)
            await ws.send('Your data has been required')