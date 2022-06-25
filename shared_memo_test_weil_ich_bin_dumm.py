from multiprocessing import shared_memory
from threading import Thread, Semaphore
import random
import time

# Creating the Shared Memory with a Byte size of 10
shared_mem_1 = shared_memory.SharedMemory(create=True, size=10000)
# Creating my Semaphore
sema_Conv, sema_Log, sema_Stat, sema_Report = Semaphore(1), Semaphore(0), Semaphore(0), Semaphore(0)


# Creating a random number while the Semaphore allows it writing it into the shared memory block
class Conv(Thread):
    def run(self):
        while True:
            sema_Conv.acquire()
            num = str(((random.sample(range(1, 10), 1))))
            verarbeiten = str(num)
            nummer = int(verarbeiten.strip('[]'))
            b = bytes(100)
            for i, c in enumerate(b, nummer):
                shared_mem_1.buf[0] = nummer
            sema_Log.release()


class Log(Thread):
    def run(self):
        while True:
            sema_Log.acquire()
            file = open("file_SHM_S.txt", "w")
            content = str(shared_mem_1.buf[0])
            file.write(content)
            file.close()
            sema_Stat.release()


num_list = []


class Stat(Thread):
    def run(self):
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


class Report(Thread):
    def run(self):
        while True:
            sema_Report.acquire()
            time.sleep(2)
            print("The Sum is : " + str(shared_mem_1.buf[0]))
            print("The Mean is : " + str(shared_mem_1.buf[1]))
            sema_Conv.release()


conv = Conv();
log = Log();
stat = Stat();
report = Report()
conv.start();
log.start();
stat.start();
report.start()
