import socket
import random
import multiprocessing

import time
from time import sleep

IP = socket.gethostbyname(socket.gethostname())
PORT = 4444
ADDRESS = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def conv():
    a = random.randint(0, 10000)
    return a


def log(arg):
    file = open("File.txt", "a")
    variable = str(arg)
    file.write(variable + '\n')
    file.close()

def stat(arg, numbers):
    numbers.append(arg)
    summe = (sum(numbers))
    mittelWert = (summe / len(numbers))
    werte = [summe, mittelWert]
    return werte

def report(arg):
    print("Summe , Mittelwert ", arg)


def main():
    array = []
    while True:

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDRESS)

        file = open("File.txt", "r")

        if __name__ == '__main__':
            pro = []
            variable = conv()
            extraVariable = variable
            variable2 = stat(extraVariable, array)


            p2 = multiprocessing.Process(target=log, args=(variable,))
            p4 = multiprocessing.Process(target=report, args=(variable2,))
            pro.append(p2)
            pro.append(p4)
            p2.start()
            p4.start()
            time.sleep(1)

            for p in pro:
                p.join()


        data = file.read()
        client.send("File.txt".encode(FORMAT))
        message = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {message}")

        client.send(data.encode(FORMAT))
        message = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {message}")

        file.close()
        client.close()


if __name__ == "__main__":
    main()
