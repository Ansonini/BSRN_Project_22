import os
import random
import time
from multiprocessing import Queue

q = Queue(10)
q2 = Queue(10)
q3 = Queue()
q4 = Queue()
pid = os.fork()
if pid < 0:
    print("fork hat nicht funktioniert")

if pid > 0:

    pid2 = os.fork()

    if pid2 > 0:
        print("Elternprozess =  Conv  ")

        while True:
            n = random.sample(range(1, 1000), 1)
            q.put(n)
            q2.put(n)
            if q.full():
                break

    if pid2 == 0:
        time.sleep(0.5)
        print("Kindprozess2 = Log")
        file = open("file2.txt", "a")
        for num in range(q.qsize()):
            content = q.get(num)

            file.write(str(content))
            print("\nContent in file2.txt:\n", content)
        file.close()

if pid == 0:
    pid3 = os.fork()
    if pid3 > 0:
        time.sleep(1)
        print("Kindprozess1 = Stat")

        print("q2size", q2.qsize())
        q2größe = int(q2.qsize())
        numbers = []
        for i in range(q2.qsize()):
            verarbeiten = str(q2.get(i))
            numbers.append(int(verarbeiten.strip('[]')))
        summe = sum(numbers)
        mittelWert = (summe / q2größe)
        q3.put(summe)
        q4.put(mittelWert)

    if pid3 == 0:
        time.sleep(2)
        print("Kindprozess von Kindprozess1 = Report")
        print("Summe", q3.get())
        print("Mittelwert", q4.get())
