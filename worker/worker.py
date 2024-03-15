import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    while True:
        message = json.loads(r.blpop('sender')[1])

        print('Sending message: ', message['subject'])
        sleep(randint(10, 20))
        print('Message', message['subject'], 'sended!')