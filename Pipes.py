## Dennis Gerstung
## 1394582

#Os für fork und pipe
import os
#Random für den Random-Number-Generator
import random

#Erste Pipe für Kommunikation zwischen "Parent" und "Child1"
r, w = os.pipe()
#Erstellen vom Ersten Kind (Parent - Child1)
pid = os.fork()

#Zweite Pipe für Kommunikation zwischen "Parent
r2, w2 = os.pipe()

#Elternprozess
if pid != 0:

    #Erstellung vom zweiten Kind (Parent - Child2)
    pid2 = os.fork()

    # Elternprozess (Conv)
    if pid2 != 0:
        print("Parent")
        # Read-Seite von Pipe1 und Pipe2 schließen, sodass geschrieben werden kann
        os.close(r)
        os.close(r2)
        #Random-number-generator
        zahlenstring = str(random.randint(1, 1000))
        #Konvertieren von einen String in bytes, da nur bytes in Pipe möglich
        pipe1 = zahlenstring.encode()
        pipe2 = zahlenstring.encode()
        #Schreiben der bytes in das Pipe (über die write-Seite)
        os.write(w, pipe1)
        os.write(w2, pipe2)

    #Kindprozess (Log)
    if pid2 == 0:
        print("Child2")
        #Schließen der read-Seite von Pipe2
        os.close(w2)
        #Öffnen der Read-Seite von Pipe2
        r2 = os.fdopen(r2)
        #txt-Dokument wird erstellt und die Zahl(-en) hinein geschrieben
        file = open("file.txt", "w")
        file.write(r2.read())
        file.close()

#Kindprozess (vom ersten fork)
if pid == 0:
    #Erstellen der beiden Pipes zur Kommunikation zwischen "Child1 und Enkel
    r3, w3 = os.pipe()
    r4, w4 = os.pipe()
    os.close(w)
    #Erstellen des Enkels ("Child from Child")
    pid3 = os.fork()

    #Elternprozess (Stat)
    if pid3 != 0:
        #Speichern von read Seite der Pipe
        r = os.fdopen(r)
        verarbeiten = int(r.read())
        #Anlegen eines Array zum Speichern der Zahlen aus der Pipe und berechnen der Summer, sowie Durchschnitt (100 bereits hinzugefügt zur Demostartion von Funktionen)
        numbers = [100]
        numbers.append(verarbeiten)
        Sum = sum(numbers)
        mittelWert = (Sum / len(numbers))
        #Umwandeln in String zur Encodierung für die Pipes
        String1 = str(Sum)
        String2 = str(mittelWert)
        os.close(r3)
        os.close(r4)
        print("Child1")
        pipe3 = String1.encode()
        pipe4 = String2.encode()
        #Schreiben des Durchschnitts und der Summe in 2 Pipes
        os.write(w3, pipe3)
        os.write(w4, pipe4)
    #Kindprozess (Report)
    if pid3 == 0:
        os.close(r)
        print("Child from Child")
        os.close(w3)
        os.close(w4)
        #Öffnen der Pipes zur Ausgabe der Werte
        r3 = os.fdopen(r3)
        print("Summe: ", r3.read())
        r4 = os.fdopen(r4)
        print("Mittelwert: ", r4.read())