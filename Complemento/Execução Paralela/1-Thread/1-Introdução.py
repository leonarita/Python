import _thread


def filho (tid):
    print('Olá da thread', tid)


def pai():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(filho, (i, ))

        if input() == 'q':
            break


pai()