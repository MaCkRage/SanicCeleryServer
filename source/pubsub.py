import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()


#  функция _callback для теста
def _callback(message):
    print(f'message: {message}')


def subscribe(channel, callback):
    p.subscribe(**{f'{channel}': callback})
    # while True:
    message = p.get_message()
    print(message)


def publish(channel, message):
    r.publish(channel, message)


print('start')
print('subscribe')
subscribe(channel='first_channel', callback=_callback)
print('publish')
publish(channel='first_channel', message='hello')
print('_callback')
_callback(message=p.get_message())
print('end')
