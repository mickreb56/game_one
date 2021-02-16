from math import *
from array import *
from random import *
from time import *
import threading
vec = [0,0]

def piCount(size):
    for i in range(100000):
        point = [randint(-1*size,size), randint(-1*size,size)]
        
        var = sqrt((point[0]) ** 2 + (point[1]) ** 2)
        if(var <= size):
            vec[0] += 1
        else:
            vec[1] += 1

def main():
    time = perf_counter()
    threads = 100
    iterations = 10
    circleDiamiter = 1000000
    print("~~~~~Working~~~~~")
    for i in range(iterations):
        t = []
        for j in range(threads):
            t.append(threading.Thread(target=piCount, args=(circleDiamiter,)))
        for j in range(threads):
            t[j].start()
        for j in range(threads):
            t[j].join()
        t.clear()
        temp = vec[0]/vec[1]
        print("pi calc       : ", temp)
        print("%pi           : ", (temp/pi)*100)
        print("total itration: ", vec[0] + vec[1])
        print("time passed   : ", perf_counter() - time, "\n")

        time = perf_counter()

main()