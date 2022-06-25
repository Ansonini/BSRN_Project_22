from multiprocessing import shared_memory

shm_a = shared_memory.SharedMemory(name='shared_memory', create=True, size=12)

for i, c in enumerate(b"Hello world"):
    shm_a.buf[i] = c

while True:
    try:
        pass
    except KeyboardInterrupt:
        break

print(bytes(shm_a.buf[:12]))
shm_a.close()
shm_a.unlink()
