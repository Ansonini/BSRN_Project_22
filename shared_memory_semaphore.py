import os
import multiprocessing
import threading
import random
import time

PROCESS_ID = os.fork()

if PROZESS_ID != 0:

    PROCESS_ID2 = os.fork()

    if PROZESS_ID2 != 0:
        print("Parent")
    else:  # PROCESS_ID2 == 0
        print("Child2")

else:  # PROCESS_ID == 0

    PROCESS_ID3 = os.fork()
    if PROZESS_ID3 != 0:
        print("Child1")
    else:  # PROCESS_ID3 == 0
        print("Child from Child")
