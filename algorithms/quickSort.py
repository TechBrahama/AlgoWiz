import time
from colors import *

comparission =0
def partition(data, start, end, drawData, timeTick, num_of_cmp):
    i = start + 1
    pivot = data[start]
    global comparission
    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
        comparission+=1
        num_of_cmp(comparission)
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quick_sort(data, start, end, drawData, timeTick, num_of_cmp):
    if start < end:
        pivot_position = partition(data, start, end, drawData, timeTick, num_of_cmp)
        quick_sort(data, start, pivot_position-1, drawData, timeTick, num_of_cmp)
        quick_sort(data, pivot_position+1, end, drawData, timeTick, num_of_cmp)

        drawData(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                        else DARK_BLUE if x > pivot_position and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, [BLUE for x in range(len(data))])
