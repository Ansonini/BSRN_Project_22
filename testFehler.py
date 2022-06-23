import random
import numpy
from numpy import mean, sum


class Conv:                         #Random Number generator
    random_num = []
    n = random.sample(range(1, 1000), 5)

    #n = 10
    #n in Pipe rein
    random_num.append(n)
    print(random_num)


class Log:                          #Random nummer von CONV wird in file gespeichert
    with open("file.txt", "w") as file:
        file.write("".join(str(x) for x in Conv.n))         #Liste mit Int in STring und dann in file
        file.write("\n")
        file.close()



class Stat:                         #Start wertet die Daten aus
    sum = sum(Conv.random_num)
    avg = mean(Conv.random_num)
    #pipe raus -- n
    # x = n



class Report:                       #Report gibt die Daten wider
    print("\nThe sum of List is:\n", Stat.sum)
    print("\nThe average of List is:\n", Stat.avg)

