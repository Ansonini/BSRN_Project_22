import os
from multiprocessing import shared_memory
from threading import Semaphore, BoundedSemaphore
import random
import time

# Create Parent process ID
PROCESS_ID = os.fork()
# Creating my Semaphore
sema = Semaphore
# Creating the Shared Memory with a Byte size of 10
shared_mem_1 = shared_memory.SharedMemory(name='shared_memory', create=True, size=10)

if PROZESS_ID != 0:

    PROCESS_ID2 = os.fork()

    if PROZESS_ID2 != 0:
        print("Parent")
        # Creating a random number while the Semaphore allows it writing it into the shared memory block
        while sema <= 0:
            num = random.sample(range(1, 1000), 1)
            shared_mem_1[0] = num

    else:  # PROCESS_ID2 == 0
        print("Child2")
        # Taking the num out of the memory block and putting it into the file
        file = open("file_SHM_S.txt", "w")
        file.write(shared_mem_1[0])
        file.close()

# Child of the first process
else:  # PROCESS_ID == 0
    # Creating a ShadeMemory List appending all the num generated from Conv
    num_list = []
    num_list.append(shared_memory[0])
    sum_num = sum(num_list)
    mean_num  = sum_num/len(sum_num)
    shared_mem_1[0] = sum_num
    shared_mem_1[1] = mean_num

    PROCESS_ID3 = os.fork()
    if PROZESS_ID3 != 0:
        print("Child1")
        # Print Sum from report
        print("The Sum is : " + shared_mem_1[0])

    else:  # PROCESS_ID3 == 0
        # Print Mean from report
        print("The Mean is : " + shared_mem_1[1])
        print("Child from Child")
