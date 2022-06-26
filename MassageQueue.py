## Alexander Kunkel
## 1397709

# Implementierung
import os
import random
import time
from multiprocessing import Queue

# Erstellung Queues
q = Queue(10)
q2 = Queue(10)
q3 = Queue()
q4 = Queue()
# Erster Prozess wird erstellt
pid = os.fork()
# Fehler Meldung
if pid < 0:
    print("fork hat nicht funktioniert")
# Klarstellung, dass es sich um den Elternprozess von pid handelt
if pid > 0:
    # Erstellung vom zweiten Prozess
    pid2 = os.fork()
    # Klarstellung, dass es sich um den Elternprozess von pid2 handelt
    if pid2 > 0:
        print("Elternprozess =  Conv  ")
        # Conv
        while True:
            n = random.sample(range(1, 1000), 1)
            q.put(n)
            q2.put(n)
            if q.full():
                break
    # Klarstellung, dass es sich um den Kindprozess von pid2 handelt
    if pid2 == 0:
        # Log
        time.sleep(0.5)
        print("Kindprozess2 = Log")
        file = open("file2.txt", "a")
        for num in range(q.qsize()):
            content = q.get(num)
            file.write(str(content))
            print("\nContent in file2.txt:\n", content)
        file.close()
# Klarstellung, dass es sich um den kindprozess von pid handelt
if pid == 0:
    # Erstellung eines neuen Prozesses (wichtig da Stat nicht nur Kind- sondern auch Elternprozess ist)
    pid3 = os.fork()
    # klarstellung, dass es sich um den Elternprozess von pid3 handelt
    if pid3 > 0:
        # Stat
        time.sleep(1)
        print("Kindprozess1 = Stat")
        print("q2size", q2.qsize())
        q2größe = int(q2.qsize())
        numbers = []
        # Umwandlung von Elementen in q2 von str zu int
        for i in range(q2.qsize()):
            verarbeiten = str(q2.get(i))
            numbers.append(int(verarbeiten.strip('[]')))
        summe = sum(numbers)
        mittelWert = (summe / q2größe)
        q3.put(summe)
        q4.put(mittelWert)
    # Klarstellung, dass es sich um den Kindprozess von pid3 handelt
    if pid3 == 0:
        # Report
        time.sleep(2)
        print("Kindprozess von Kindprozess1 = Report")
        print("Summe", q3.get())
        print("Mittelwert", q4.get())
