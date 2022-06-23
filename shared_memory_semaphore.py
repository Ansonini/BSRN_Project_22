import os
import multiprocessing
import threading
import random
import time

PROZESS_ID = os.fork()


if PROZESS_ID != 0:

    PROZESS_ID2 = os.fork()

    if PROZESS_ID2 != 0:
        print("Parent")


    if PROZESS_ID2 == 0:
        print("Child2")


if PROZESS_ID == 0:

    PROZESS_ID3 = os.fork()
    if PROZESS_ID3 != 0:
        print("Child1")


    if PROZESS_ID3 == 0:
        print("Child from Child")