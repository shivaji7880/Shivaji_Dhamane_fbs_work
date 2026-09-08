import threading
import time
import random

buffer = []
MAX_SIZE = 5

condition = threading.Condition()

def producer(name):
    for i in range(5):
        item = random.randint(1, 100)

        with condition:
            while len(buffer) == MAX_SIZE:
                condition.wait()

            buffer.append(item)
            print(name, "produced:", item)

            condition.notify_all()

        time.sleep(0.5)

def consumer(name):
    for i in range(5):
        with condition:
            while len(buffer) == 0:
                condition.wait()

            item = buffer.pop(0)
            print(name, "consumed:", item)

            condition.notify_all()

        time.sleep(0.5)

p1 = threading.Thread(target=producer, args=("Producer-1",))
p2 = threading.Thread(target=producer, args=("Producer-2",))

c1 = threading.Thread(target=consumer, args=("Consumer-1",))
c2 = threading.Thread(target=consumer, args=("Consumer-2",))

p1.start()
p2.start()
c1.start()
c2.start()


p1.join()
p2.join()
c1.join()
c2.join()

print("Done")