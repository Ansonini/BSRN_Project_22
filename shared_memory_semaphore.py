import os
from multiprocessing import shared_memory
from threading import Semaphore, BoundedSemaphore
import random
import time

# Creating my Semaphore
sema = Semaphore(1)
sema_Conv, sema_Log, sema_Stat, sema_Report = Semaphore(0), Semaphore(1), Semaphore(1), Semaphore(1)
# Create Parent process ID
PROZESS_ID = os.fork()
# Creating the Shared Memory with a Byte size of 10
shared_mem_1 = shared_memory.SharedMemory(name='shared_memory', create=True, size=10)

# Parent Process
if PROZESS_ID != 0:

    # Second Child Created
    PROZESS_ID2 = os.fork()

    # Parent
    if PROZESS_ID2 != 0:
        print("Parent")
        # Creating a random number while the Semaphore allows it writing it into the shared memory block
        #Conv

    # Child 2
    else:  # PROCESS_ID2 == 0
        print("Child2")
        # Taking the num out of the memory block and putting it into the file
        #Log

# Child1 Process

else:  # PROCESS_ID == 0
    # Creating a ShadeMemory List appending all the num generated from Conv

    # Child of Child1 (Now Parent)
    PROZESS_ID3 = os.fork()

    # Child1 (now Parent from Child PROZESS_ID3)
    if PROZESS_ID3 != 0:
        print ("Child1 (now Parent of Child_of_Child")
        #STAT

    #Child of Child1
    else:  # PROCESS_ID3 == 0
        print("Child from Child")

        #REPORT

        # Print Mean from report
        print("Child1")
            # Print Sum and Mean from report

