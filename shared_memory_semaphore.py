import os
from multiprocessing import shared_memory
from threading import Semaphore, BoundedSemaphore
import random
import time

from multiprocessing import shared_memory
from threading import Thread, Semaphore
import random
import time

# Creating the Shared Memory with a Byte size of 10
shared_mem_1 = shared_memory.SharedMemory(create=True, size=10000)
# Creating my Semaphore
sema_Conv, sema_Log, sema_Stat, sema_Report = Semaphore(1), Semaphore(0), Semaphore(0), Semaphore(0)

log = Log();
stat = Stat();
report = Report()

log.start();
stat.start();
report.start()

# Create Parent process ID
PROZESS_ID = os.fork()

# Parent Process
if PROZESS_ID != 0:

    # Second Child Created
    PROZESS_ID2 = os.fork()

    # Parent
    if PROZESS_ID2 != 0:
        print("Parent")
        # Creating a random number while the Semaphore allows it writing it into the shared memory block
        # Conv
        while True:
            sema_Conv.acquire()
            num = str(((random.sample(range(1, 10), 1))))
            verarbeiten = str(num)
            nummer = int(verarbeiten.strip('[]'))
            b = bytes(100)
            for i, c in enumerate(b, nummer):
                shared_mem_1.buf[0] = nummer
            sema_Log.release()
    # Child 2
    else:  # PROCESS_ID2 == 0
        print("Child2")
        # Taking the num out of the memory block and putting it into the file
        # Log
        while True:
            sema_Log.acquire()
            file = open("file_SHM_S.txt", "a")
            content = str(shared_mem_1.buf[0])
            file.write(content)
            file.close()
            sema_Stat.release()

# Child1 Process

else:  # PROCESS_ID == 0
    # Creating a ShadeMemory List appending all the num generated from Conv

    # Child of Child1 (Now Parent)
    PROZESS_ID3 = os.fork()

    # Child1 (now Parent from Child PROZESS_ID3)
    if PROZESS_ID3 != 0:
        print("Child1 (now Parent of Child_of_Child")
        # STAT
        while True:
            sema_Stat.acquire()
            num_list.append(shared_mem_1.buf[0])
            sum_num = sum(num_list)
            mean_num = sum_num / len(num_list)
            mean_num = int(mean_num)
            b = bytes(1)
            for i, c in enumerate(b, sum_num):
                shared_mem_1.buf[0] = sum_num
            shared_mem_1.buf[1] = mean_num
            sema_Report.release()

    # Child of Child1
    else:  # PROCESS_ID3 == 0
        print("Child from Child")

        # REPORT
        while True:
            sema_Report.acquire()
            time.sleep(2)
            print("The Sum is : " + str(shared_mem_1.buf[0]))
            print("The Mean is : " + str(shared_mem_1.buf[1]))
            print("\n")
            sema_Conv.release()
        # Print Mean from report
        print("Child1")
        # Print Sum and Mean from report
