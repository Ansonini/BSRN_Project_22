from multiprocessing import shared_memory
from threading import Semaphore, BoundedSemaphore
import random
import time

# Creating the Shared Memory with a Byte size of 10
shared_mem_1 = shared_memory.SharedMemory(create=True, size=10)
# Creating my Semaphore
sema = Semaphore(1)



# Creating a random number while the Semaphore allows it writing it into the shared memory block
while True:
    sema.acquire()
    num = (random.sample(range(1, 250), 1))
    print("num", num)
    shared_mem_1.buf[0] = num
    print(shared_mem_1.buf[0])
    sema.release()
