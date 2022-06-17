import time
from time import sleep
from signal import signal, SIGINT
from sys import exit
import os
import sys

import server
import client

def handler(signal_received, frame):
    print('\nCTRL+C WURDE GEDRÜCKT, das Programm endet')
    #kill(pid, signal.SIGEND)
    exit(0)


if __name__ == '__main__':
    signal(SIGINT, handler)

    print('\n[LÄUFT. Drücken Sie CTRL-C um Programm zu stoppen!]\n')
    txt = "Hallo, dieses Programm betrachtet das Thema 'Interprozesskommunikation'\n"
    for i in txt:
        time.sleep(0.1)
        print(i, end='', flush=True)
    txt = "Sie haben den Wahl, den Datenaustausch zwischen vier Prozessen durch 'Pipes' , 'Message Queues','Shared Memory' oder 'Sockets' durchzuführen \n"
    for i in txt:
        time.sleep(0.05)
        print(i, end='', flush=True)
    time.sleep(1)
    cmd = ""
    while True:
        print("WAHL:\n    "
              "Tippen Sie 'p' ein, wenn sie wollen, Pipes nutzen\n    "
              "Tippen Sie 'mq' ein, wenn sie wollen Message Queues nutzen\n    "
              "Tippen Sie 'sm' ein, wenn sie wollen Shared Memory nutzen\n    "
              "Tippen Sie 's' ein wenn sie wollen Sockets nutzen\n    ")
        wahl = input()

        if wahl == 'p':
            print("Sie haben Pipes als Methode gewählt\n")

            

        elif wahl == 'mq':
            print("Sie haben Message Queues als Methode gewählt\n")

        elif wahl == 'sm':
            print("Sie haben Shared Memory als Methode gewählt\n")

        elif wahl == 's':
            print("Sie haben Sockets als Methode gewählt\n")

            pid = os.fork()
            if pid>0:
                print("Wir sind Eltern")
                server.main()


            elif pid == 0:
                print("Wir sind Kinder")
                server.main()

                #client.main()

        else :
            print("Sie haben was flasch eingetippt\n")
            print("Wählen Sie nochmal\n")

    while True:
        pass
