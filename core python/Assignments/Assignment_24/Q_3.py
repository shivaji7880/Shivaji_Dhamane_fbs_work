import threading

def lowercase():
    for ch in range(ord('a'), ord('z') + 1):
        print(chr(ch), end=" ")

def uppercase():
    for ch in range(ord('A'), ord('Z') + 1):
        print(chr(ch), end=" ")

t1 = threading.Thread(target=lowercase)
t2 = threading.Thread(target=uppercase)

t1.start()
print()
t2.start()

t1.join()
t2.join()

print("\nDone")