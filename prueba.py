# import sched
# import time

# scheduler = sched.scheduler(time.time, time.sleep)


# def print_event(name, start):
#     now = time.time()
#     elapsed = int(now - start)
#     print('EVENT: {} elapsed={} name={}'.format(
#         time.ctime(now), elapsed, name))


# start = time.time()
# print('START:', time.ctime(start))
# scheduler.enter(2, 1, print_event, ('first', start))
# scheduler.enter(3, 1, print_event, ('second', start))

# scheduler.run()

from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=21, minute=28, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print("hello world")
    #...

t = Timer(secs, hello_world)
t.start()
