import threading
from threading import *

print(current_thread().getName())

def mt():
    print('child thread\n')

child = Thread(target=mt)
child.start()

print('Executing thread name: ',current_thread().getName())