import random
import threading
import numpy
from  queue import  Queue
from numpy import mean, sum


class Conv:
    random_num = []
    n = random.sample(range(1, 1000), 5)
    random_num.append(n)
    print(random_num)


class Log:
    for num in range(len(Conv.random_num)):
        file = open("file.txt", "w")
        content = str(Conv.random_num)
        file.write(content)
        file.close()
        file = open("file.txt", "r")
        content = file.read()
        print("\nContent in file.txt:\n", content)
        file.close()


class Stat:
    sum = sum(Conv.random_num)
    avg = mean(Conv.random_num)


class Report:
    print("\nThe sum of List is:\n", Stat.sum)
    print("\nThe average of List is:\n", Stat.avg)


q = Queue()
q.put(str(Conv.random_num))
q.put(Conv.random_num)
q.put(Conv.random_num)
Log.content = q.get()
print(Log.content)

summe= sum(q.get())
avgerege= mean(q.get())
q.put(summe)
q.put(avgerege)
print(q.get())
print(q.get())

q = Queue(maxsize=100)

def worker():
    while True:
        item = q.get()
        print(f'Am Arbeiten {item}')
        print(f'Fertig {item}')
        q.task_done()


threading.Thread(target=worker, daemon=True).start()


for item in range(1001):
    q.put(item)


q.join()
print('Alles fertig!')



