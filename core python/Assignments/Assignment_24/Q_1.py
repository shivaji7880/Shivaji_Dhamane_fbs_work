import threading

results = [0, 0, 0, 0]

def sum_of_squares(start, end, index):
    total = 0

    for i in range(start, end + 1):
        total = total + i * i

    results[index] = total


t1 = threading.Thread(target=sum_of_squares, args=(1, 25, 0))
t2 = threading.Thread(target=sum_of_squares, args=(26, 50, 1))
t3 = threading.Thread(target=sum_of_squares, args=(51, 75, 2))
t4 = threading.Thread(target=sum_of_squares, args=(76, 100, 3))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

total = sum(results)

print("Sum of squares from 1 to 100 =", total)