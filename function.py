import random
from numpy import mean, sum

def Conv():
    random_num = []
    num = random.sample(range(0,1000), 10)
    random_num.append(num)
    print(random_num)


class ConvClass:
    random_num = []
    n = random.sample(range(1, 1000), 5)
    random_num.append(n)
    print(random_num)

def Log():
    for num in range(len(Conv.random_num)):
        f = open("BSRN_file.txt", "w")
        content = str(Conv.random_num)
        f.write(content)
        f.close()

def LogRead():
    f = open("BSRN_file.txt", "r")
    output = f.read()
    print("\n Checking  for text   read \n" + output)
    f.close()

class LogClass:
    for num in range(len(Conv.random_num)):
        file = open("file.txt", "w")
        content = str(Conv.random_num)
        file.write(content)
        file.close()
        file = open("file.txt", "r")
        content = file.read()
        print("\nContent in file.txt:\n", content)
        file.close()

def Stat():
    sum_num = sum(Conv.random_num)
    average_num = mean(Conv.random_num)

def Report_Stat(sum_num, average_num):
    print(sum_num)
    print(average_num)


class StatTest:
    sum = sum(Conv.random_num)
    avg = mean(Conv.random_num)


class Report:
    print("\nThe sum of List is:\n", Stat.sum)
    print("\nThe average of List is:\n", Stat.avg)