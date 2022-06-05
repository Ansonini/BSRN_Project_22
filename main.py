import random
import numpy
from numpy import mean, sum


class Conv:                         #Random Number generator
    random_num = []
    n = random.sample(range(1, 1000), 5)
    random_num.append(n)
    print(random_num)


class Log:                          #Random nummer von CONV wird in file gespeichert
    for num in range(len(Conv.random_num)):
        file = open("file.txt", "w")
        content = str(Conv.random_num)
        file.write(content)
        file.close()
        file = open("file.txt", "r")
        content = file.read()
        print("\nContent in file.txt:\n", content)
        file.close()


class Stat:                         #Start wertet die Daten aus
    sum = sum(Conv.random_num)
    avg = mean(Conv.random_num)


class Report:                       #Report gibt die Daten wider
    print("\nThe sum of List is:\n", Stat.sum)
    print("\nThe average of List is:\n", Stat.avg)

