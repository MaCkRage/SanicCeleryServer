import os
import redis


REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
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
