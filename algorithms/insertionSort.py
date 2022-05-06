import time
from colors import *

def insertion_sort(data, drawData, timeTick, num_of_cmp):
    comparission = 0
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k-1]:
            data[k] = data[k-1]
            k -= 1
            comparission+=1
        data[k] = temp
        comparission+=1
        num_of_cmp(comparission)
        drawData(data, [YELLOW if x == k or x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, [BLUE for x in range(len(data))])
