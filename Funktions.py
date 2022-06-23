import test
import time

y = 1

while True:
    print("Programm wurde gestartet")
    print(y, "RUNDE-")
    test.funktionLog(test.funktionConv())
    test.funktionReport(test.funktionStat())

    print(y, "Runde ist vorbei, ", y + 1, "Runde startet in 5 Sekunden")
    y = y + 1
    print("Um Programm zu beenden tippen Sie Strg + C ein")

    time.sleep(5)
