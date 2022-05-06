import time
from colors import *


cmp = 0 
def linear_search(data, drawData, timeTick, num_of_cmp, element):
    size = len(data)
    y = int(element)
    index = -1
    global cmp
    cmp =0
    for i in range(size):
        colors =[]
        cmp +=1
        if data[i] == y:
            for x in range(size):
                if x < i:
                    colors.append(YELLOW)
                elif x == i:
                    colors.append(BLACK)
                else:
                    colors.append(RED)
            drawData(data,colors)
            element_found = str(cmp)+"\nElement found!!! "
            num_of_cmp(element_found)
            index = i
            break
        else:
            for x in range(size):
                if x <= i:
                    colors.append(YELLOW)
                else:
                    colors.append(RED)
            drawData(data,colors)
            element_found = str(cmp)+"\nElement not found!!!"
            num_of_cmp(element_found)
        time.sleep(timeTick)

    if index == -1:
        print("not found")
    else:
        print("found at"+str(index+1))
            
        
    
    