from redis import Redis
import translate, time
from rq import Connection, Queue

q = Queue(connection=Redis())

result = q.enqueue(
             translate.spanish, 'hello')

time.sleep(3)

print result.result
