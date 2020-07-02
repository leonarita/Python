import threading

class Minhathread(threading.Thread):
    def __init__(self, meuId, cont, mutex):
        self.meuId = meuId
        self.cont = cont
        self.mutex = mutex
        threading.Thread.__init__(self)

    # Override
    def run(self):
        for i in range(self.cont):
            with self.mutex:
                print('[%s] => %s' % (self.meuId, i))


stdoutmutex = threading.Lock()
threads = []

for i in range(10):
    thread = Minhathread(i, 100, stdoutmutex)

    # start chama método run
    thread.start()

    threads.append(thread)

# Finaliza a thread
for thread in threads:
    thread.join()

print('Saindo da Thread principal.')
