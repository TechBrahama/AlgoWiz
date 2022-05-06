import time
from colors import *

cmp =0 
def binary_search(data, drawData, timeTick, element, num_of_cmp):
    global cmp
    size = len(data)
    l = 0
    r = len(data) - 1
    index = -1
    colors = [RED] * (len(data))
    data.sort()
    drawData(data,colors)
    y=int(element)
    while l <= r:
        mid = l + (r - l) // 2
        colors[mid] = YELLOW
        drawData(data, colors)
        time.sleep(timeTick)
        if data[mid] == y:
            cmp += 1
            colors[mid] = BLACK
            drawData(data, colors)
            num_of_cmp(cmp)
            index = mid
            break
        elif data[mid] < y:
            l = mid + 1
            cmp += 1
            for i in range(mid + 1):
                colors[i] = WHITE
            drawData(data, colors)
            num_of_cmp(cmp)
        else:
            r = mid - 1 
            cmp += 1
            for i in range(mid, len(data)):
                colors[i] = WHITE
            drawData(data, colors)
            num_of_cmp(cmp)
        time.sleep(timeTick)
    if index == -1:
        found = str(cmp)+"\nElement Not Found!!!"
        num_of_cmp(found)
        print("Not Found")
    else:
        found = str(cmp)+"\nElement Found!!!"
        num_of_cmp(found)
        print("Found")

