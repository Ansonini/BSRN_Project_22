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

def Log(random_num):
    for num in range(len(random_num)):
        f = open("BSRN_file.txt", "w")
        content = str(random_num)
        f.write(content)
        f.close()

def LogRead():
    f = open("BSRN_file.txt", "r")
    output = f.read()
    print("\n Checking  for text   read \n" + output)
    f.close()

class LogClass:
    for num in range(len(ConvClass.random_num)):
        file = open("file.txt", "w")
        content = str(ConvClass.random_num)
        file.write(content)
        file.close()
        file = open("file.txt", "r")
        content = file.read()
        print("\nContent in file.txt:\n", content)
        file.close()

def Stat(random_num):
    sum_num = sum(random_num)
    average_num = mean(random_num)

def Report_Stat(sum_num, average_num):
    print(sum_num)
    print(average_num)


class StatTest:
    sum = sum(ConvClass.random_num)
    avg = mean(ConvClass.random_num)


class Report:
    print("\nThe sum of List is:\n", StatTest.sum)
    print("\nThe average of List is:\n", StatTest.avg)

print("\n Test func")

Conv()
Log(Conv())
Stat(Conv())
Report_Stat(Stat())
