import random

def funktionConv():
    a = random.randint(0, 100000)
    print("Die Zahl ist", a)
    return a


def funktionLog(arg):
    file = open("File.txt","a")
    variable = str(arg)
    file.write(variable + '\n')
    print("Die Zahl wurde in Datei geschpeichert")
    file.close()
    print()


def funktionStat():
    file = open("File.txt", "r")
    numbers = []

    for line in file:
        numbers.append(int(line))
    print("Diese Zahlen wurden in Datei eingespeichert")
    print(numbers)
    summe=(sum(numbers))
    mittelWert=(summe/len(numbers))
    werte = []
    werte.append(summe)
    werte.append(mittelWert)
    return werte


def funktionReport(arg):
    print("Summe Aller Zahlen, die in der Datei stehen:")
    print(arg[0])
    print()
    print("Mittelwert Aller Zahlen, die in der Datei stehen:")
    print(round(arg[1]))
    print()

