from math import *
from array import *
from random import *
from time import *
import threading
vec = [0,0]

def piCount():
    for i in range(10000):
        point = [randint(0,1000), randint(0,1000)]
        
        var = sqrt((point[0] - 500.0) ** 2 + (point[1] - 500.0) ** 2)
        if(var <= 500.0):
            vec[0] += 1
        else:
            vec[1] += 1
    return vec

def main():
    time = perf_counter()
    count = 50
    for i in range(10):
        t = []
        for j in range(count):
            t.append(threading.Thread(target=piCount))
        for j in range(count):
            t[j].start()
        for j in range(count):
            t[j].join()
        temp = vec[0]/vec[1]
        print("pi: ", temp)
        print("%pi: ", (pi/temp)*100)
        print("time: ",perf_counter() - time)
        print(vec,"\n")
        time = perf_counter()

main()