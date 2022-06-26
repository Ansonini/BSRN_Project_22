## Lucian Zimmermann
# 1400243

## Shared Memory with Semaphores with Parent-Child Fork

import os
from multiprocessing import shared_memory
from threading import Semaphore, Thread
import random
import time

# Creating the Shared Memory with a Byte size of 10
shared_mem_1 = shared_memory.SharedMemory(create=True, size=10)
# Creating my Semaphored for every process
# Semaphore setting Conv to 1, Log to 0, Stat to 0 and Report to 0
sema_Conv, sema_Log, sema_Stat, sema_Report = Semaphore(1), Semaphore(0), Semaphore(0), Semaphore(0)


# Creating a random number while the Semaphore allows it, writing it into the shared memory block
class Conv(Thread):
    def run(self):
        while True:
            # lock the Conv Semaphore = 0
            sema_Conv.acquire()
            # generating a random number between 1 and 10
            num = str(((random.sample(range(1, 10), 1))))
            verarbeiten = str(num)
            # geht den erstellten string durch und kürzt die [ ] um die zahl herum weck
            nummer = int(verarbeiten.strip('[]'))
            # fügt die random zahl in den memory block an Platz 1
            shared_mem_1.buf[0] = nummer
            # unlocking the Log Semaphore = 1
            sema_Log.release()


# Creating a file, if not yet existent, and adding the random number generated by conv
# and given through the shared memory block if the Semaphore allows access
class Log(Thread):
    def run(self):
        while True:
            # lock the Log Semaphore = 0
            sema_Log.acquire()
            # öffnet/erstellt eine file mit dem namen "file_SHM_S.txt" mit anhänge recht
            file = open("file_SHM_S.txt", "a")
            # die zahl weird aus shared_mem_1.buf[0] ausgelesen und in einen String gecastet
            content = str(shared_mem_1.buf[0])
            # danach werden die zahl in die file "file_SHM_S.txt" geschrieben
            # und die "file_SHM_S.txt" wird geschlossen
            file.write(content)
            file.close()
            # unlock the log Semaphore = 1
            sema_Stat.release()


# creating a list of numbers to store the all the numbers created by Conv to use in creating the sum

num_list = []


# Uses the number created in Conv and takes it out of the Shared Memory putting it into a list and through the list
# calculates the Sum of all the numbers created by Conv and saved into the list and calculates the mean
# of all the numbers. Then it saves the sum of the numbers in shared_mem_1.buf[0]
# and saves the mean in shared_mem_1.buf[1] if the semaphore allows access
class Stat(Thread):
    def run(self):
        while True:
            # lock the Stat Semaphore = 0
            sema_Stat.acquire()
            # puts the number into the list
            num_list.append(shared_mem_1.buf[0])
            sum_num = sum(num_list)
            mean_num = sum_num / len(num_list)
            mean_num = int(mean_num)
            # declarer b als 1 byte
            b = bytes(1)
            # adds the sum into the shared memory at position 1
            for i, c in enumerate(b, sum_num):
                shared_mem_1.buf[0] = sum_num
            shared_mem_1.buf[1] = mean_num
            # unlock the Report Semaphore = 1
            sema_Report.release()


# Takes the first to numbers from shared_mem_1.buf[0] and shared_mem_1.buf[1] and prints them out to the console
# if the Semaphore allows access
class Report(Thread):
    def run(self):
        while True:
            # lock the Report Semaphore = 0
            sema_Report.acquire()
            # puts the program to sleep for 2 seconds so that the
            time.sleep(2)
            # printing the Sum and the Mean to the console together with a Line in between to make it easier to read
            print("The Sum is : " + str(shared_mem_1.buf[0]))
            print("The Mean is : " + str(shared_mem_1.buf[1]))
            print("\n")
            # unlock the Conv Semaphore = 1
            sema_Conv.release()


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
        conv = Conv();
        conv.start();
    # Child 2
    else:  # PROCESS_ID2 == 0
        print("Child2")
        # Taking the num out of the memory block and putting it into the file
        # Log
        log = Log();
        log.start();
# Child1 Process

else:  # PROCESS_ID == 0
    # Creating a ShadeMemory List appending all the num generated from Conv

    # Child of Child1 (Now Parent)
    PROZESS_ID3 = os.fork()

    # Child1 (now Parent from Child PROZESS_ID3)
    if PROZESS_ID3 != 0:
        print("Child1 (now Parent of Child_of_Child)")
        # STAT
        stat = Stat();
        stat.start();
    # Child of Child1
    else:  # PROCESS_ID3 == 0
        print("Child from Child")

        # REPORT
        report = Report()
        report.start()
        # Print Mean from report
        print("Child1")
        # Print Sum and Mean from report
