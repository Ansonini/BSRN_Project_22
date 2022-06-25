import os
from multiprocessing import shared_memory
from threading import Semaphore, BoundedSemaphore
import random
import time

# Creating my Semaphore
sema = Semaphore(1)
# Create Parent process ID
PROZESS_ID = os.fork()
# Creating the Shared Memory with a Byte size of 10
shared_mem_1 = shared_memory.SharedMemory(name='shared_memory', create=True, size=10)

if PROZESS_ID != 0:

    PROZESS_ID2 = os.fork()

    if PROZESS_ID2 != 0:
        print("Parent")
        # Creating a random number while the Semaphore allows it writing it into the shared memory block
        while True:
            sema.acquire()
            num = (random.sample(range(1, 1000), 1))
            shared_mem_1.buf[0] = num
            sema.release()

    else:  # PROCESS_ID2 == 0
        print("Child2")
        # Taking the num out of the memory block and putting it into the file
        while True:
            sema.acquire()
            file = open("file_SHM_S.txt", "w")
            file.write(shared_mem_1[0])
            file.close()
            sema.release()

# Child of the first process
else:  # PROCESS_ID == 0
    # Creating a ShadeMemory List appending all the num generated from Conv
    while True:
        sema.acquire()
        num_list = []
        num_list.append(shared_memory[0])
        sum_num = sum(num_list)
        mean_num = sum_num / len(sum_num)
        shared_mem_1[0] = str(sum_num)
        shared_mem_1[1] = str(mean_num)
        sema.release()

    PROZESS_ID3 = os.fork()
    if PROZESS_ID3 != 0:
        print("Child1")
        # Print Sum from report
        while True:
            sema.acquire()
            print("The Sum is : " + shared_mem_1[0])
            sema.release()

    else:  # PROCESS_ID3 == 0
        print("Child from Child")
        # Print Mean from report
        while True:
            sema.acquire()
            print("The Mean is : " + shared_mem_1[1])
            sema.release()
