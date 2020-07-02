import threading


def gfg():
    print("Hello, world")


timer = threading.Timer(5.0, gfg)
timer.start()
