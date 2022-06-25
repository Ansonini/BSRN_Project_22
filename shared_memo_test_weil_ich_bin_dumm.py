from multiprocessing import shared_memory
from threading import Semaphore, BoundedSemaphore
import random
import time

# Creating the Shared Memory with a Byte size of 10
shared_mem_1 = shared_memory.SharedMemory(create=True, size=100)
# Creating my Semaphore
sema = Semaphore(1)


# Creating a random number while the Semaphore allows it writing it into the shared memory block
while True:
    sema.acquire()
    num = int
    num = str(((random.sample(range(1, 255), 1))))
    verarbeiten = str(num)
    nummer = int(verarbeiten.strip('[]'))

    print(type(num),)
    print("num", num)
    print(type(nummer), nummer)
    b =bytes(1)
    for i, c in enumerate(b, nummer):
        shared_mem_1.buf[0] = nummer
        print(shared_mem_1.buf[0])
    sema.release()
# Log
while True:
    sema.acquire()
