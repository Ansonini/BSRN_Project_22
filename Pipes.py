import os
import random


r, w = os.pipe()
pid = os.fork()

r2, w2 = os.pipe()

if pid != 0:

    pid2 = os.fork()

    if pid2 != 0:
        print("Parent")
        os.close(r)
        os.close(r2)
        n = random.sample(range(1, 1000), 1)
        zahlenstring = "".join(str(x) for x in n)
        pipe1 = zahlenstring.encode()
        pipe2 = zahlenstring.encode()
        os.write(w, pipe1)
        os.write(w2, pipe2)

    if pid2 == 0:
        print("Child2")
        os.close(w2)
        r2 = os.fdopen(r2)
        file = open("file.txt", "w")
        file.write(r2.read())
        file.close()

# Only changed the order here!
if pid == 0:
    r3, w3 = os.pipe()
    r4, w4 = os.pipe()
    os.close(w)
    pid3 = os.fork()
    if pid3 != 0:
        r = os.fdopen(r)
        verarbeiten = int(r.read())
        numbers = []
        numbers.append(verarbeiten)
        Sum = sum(numbers)
        mittelWert = (Sum / len(numbers))
        String1 = str(Sum)
        String2 = str(mittelWert)
        os.close(r3)
        os.close(r4)
        print("Child1")
        pipe3 = String1.encode()
        pipe4 = String2.encode()
        os.write(w3, pipe3)
        os.write(w4, pipe4)

    if pid3 == 0:
        os.close(r)
        print("Child from Child")
        os.close(w3)
        os.close(w4)
        r3 = os.fdopen(r3)
        print("Summe: ", r3.read())
        r4 = os.fdopen(r4)
        print("Mittelwert: ", r4.read())