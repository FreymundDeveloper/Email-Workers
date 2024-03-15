import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Waitning messages ...')
    while True:
        message = json.loads(r.blpop('sender')[1])

        print('Sending message: ', message['subject'])
        sleep(randint(10, 20))
        print('Message', message['subject'], 'sended!')