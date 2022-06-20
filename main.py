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

    i=0

    länge=len(Conv.random_num)
    print(länge)
    for i in range(i,5,1):
        print(i)
        queue.enqueue(Conv.random_num[i])


