import threading

condition = threading.Condition()
turn = 1


def print_odd():
    global turn

    for i in range(1, 11, 2):
        with condition:
            while turn != 1:
                condition.wait()

            print("Odd :", i)
            turn = 0
            condition.notify()


def print_even():
    global turn

    for i in range(2, 11, 2):
        with condition:
            while turn != 0:
                condition.wait()

            print("Even:", i)
            turn = 1
            condition.notify()


t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")