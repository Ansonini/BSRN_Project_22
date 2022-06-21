# This is a sample Python script.
import random
import time
from numpy import mean, sum


class Queue:

    def __init__(self):
        self.elements = []

    def enqueue(self, data):
        self.elements.append(data)
        return data

    def dequeue(self):
        return self.elements.pop(0)

    def rear(self):
        return self.elements[-1]

    def front(self):
        return self.elements[0]

    def is_empty(self):
        return len(self.elements) == 0


if __name__ == '__main__':
    queue = Queue()
    queue2 = Queue()

while True:
    ## Conv:
    while True:
        queue.enqueue(random.sample(range(1, 1000), 1))
        print(len(queue.elements))
        if len(queue.elements) > 9:
            break

    ## Log:
    content = []
    content = queue.elements
    print(content)
    for num in range(len(queue.elements)):
        file = open("file2.txt", "a")
        content = queue.dequeue()
        file.write(str(content))
        file.close()
        print("\nContent in file2.txt:\n", content)
        file.close()
        queue.enqueue(content)

    ## Stat:
    summe = sum(queue.elements)
    avg = summe / len(queue.elements)
    queue2.enqueue(summe)
    queue2.enqueue(avg)

    ## Report:
    print("Die Summe berägt: ", queue2.dequeue())
    print("Der Mittelwert beträgt", queue2.dequeue())
    ## Queue neustart
    while not queue.is_empty():
        queue.dequeue()

    time.sleep(5)









