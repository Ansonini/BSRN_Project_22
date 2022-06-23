from multiprocessing import shared_memory

sm = shared_memory.SharedMemory(create=True, size=20)

