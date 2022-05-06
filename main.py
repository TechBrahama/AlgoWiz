import re
from tkinter import *
from tkinter import ttk
import random
from tkinter.tix import IMAGETEXT
from turtle import left
from matplotlib.ft2font import BOLD
from tkinter import simpledialog 
from pil import Image, ImageTk
from numpy import blackman, pad
from algorithms import a_star
from colors import *

import os
import pygame

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort
from algorithms.linearSearch import linear_search
from algorithms.binarySearch import binary_search



# Main window 
window = Tk()
window.title("Sorting Algorithms Visualization")
#getting screen width and height of display
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()

#setting tkinter window size
window.geometry("%dx%d" % (width-10, height))
window.config(bg="#83A177")



algorithm_type = StringVar()
sort_algorithm_name = StringVar()
search_algorithm_name = StringVar()
path_algorithm_name = StringVar()
speed_name = StringVar()
data = []
user_input = 0
algo_type_list = ['Sorting', 'Searching', 'Pathfinding']
sort_algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort']
search_algo_list = ['Linear Search','Binary Search']
path_algo_list = ['A star','Dijkstra']
speed_list = ['Fast', 'Medium', 'Slow']

search_information = {'Linear Search': "Worst Case:O(n)\nAverage Case:O(n/2)\nBest Case:O(1)",
                'Binary Search': "Worst Case:O(log n)\nAverage Case:O(log n)\nBest Case:O(1)"}

sort_information = {'Bubble Sort': "Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n)",
                            'Selection Sort': "Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n²)",
                            'Merge Sort': "Worst Case:O(n*log n)\nAverage Case:O(n*log n)\nBest Case:O(n*log n)",
                            'Insertion Sort': "Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n)",
                            'Quick Sort': "Worst Case:O(n²)\nAverage Case:O(n*log n)\nBest Case:O(n*log n)",
                           }

pseudo_code = {
                'Bubble Sort': "procedure bubbleSort( list : array of items )\n"+
                                "loop = list.count;\nfor i = 0 to loop-1 do:\n   swapped = false\n   for j=0 to loop-1 do:\n"+
                                "   //Compare the adjaacent elements\n"
                                "   if list[j] > list[j+1] then\n"+"   //Swap them\n"+
                                "   swap(list[j],list[j+1])\n   swapped = true\n   end if\n"+
                                "end for \n"+"if(not swapped) then \n\tbreak \nend if\nend for\n\nend procedure return list\n",
                
                'Selection Sort': "procedure selection sort \n   list  : array of items\n   n     : size of list\n"+
                                "   for i = 1 to n - 1\n   /* set current element as minimum*/\n      min = i    \n"+
                                "      /* check the element to be minimum */\n      for j = i+1 to n\n         if list[j] < list[min] then"+
                                "            min = j;\n         end if\n      end for\n      /* swap the minimum element with the current element*/\n"+
                                "      if indexMin != i  then\n         swap list[min] and list[i]\n      end if\n   end for\nend procedure",

                'Merge Sort': "procedure mergesort( var a as array )\n   if ( n == 1 ) return a\n   var l1 as array = a[0] ... a[n/2]\n"+
                            "   var l2 as array = a[n/2+1] ... a[n]\n   l1 = mergesort( l1 )\n   l2 = mergesort( l2 )\n"+
                            "   return merge( l1, l2 )\nend procedure\nprocedure merge( var a as array, var b as array )\n"+
                            "   var c as array\n   while ( a and b have elements )\n      if ( a[0] > b[0] )\n         add b[0] to the end of c\n"+
                            "         remove b[0] from b\n      else\n         add a[0] to the end of c\n         remove a[0] from a\n"+
                            "      end if\n   end while\n   while ( a has elements )\n      add a[0] to the end of c\n      remove a[0] from a\n"+
                            "   end while\n   while ( b has elements )\n      add b[0] to the end of c\n      remove b[0] from b\n"+
                            "   end while\n   return c\nend procedure\n",

                'Insertion Sort': "procedure insertionSort( A : array of items )\n   int holePosition\n   int valueToInsert\n   for i = 1 to length(A) inclusive do:"+
                                "      \n      valueToInsert = A[i]\n      holePosition = i\n"+
                                "      /*locate hole position for the element to be inserted */\n      while holePosition > 0 and A[holePosition-1] > valueToInsert do:\n"+
                                "         A[holePosition] = A[holePosition-1]\n         holePosition = holePosition -1\n      end while\n"+
                                "      /* insert the number at hole position */\n      A[holePosition] = valueToInsert"+
                                "   end for\nend procedure",
                
                'Quick Sort': "function partitionFunc(left, right, pivot)\n   leftPointer = left\n   rightPointer = right - 1\n"+
                            "   while True do\n      while A[++leftPointer] < pivot do\n         //do-nothing\n      end while"+
                            "\n\n      while rightPointer > 0 && A[--rightPointer] > pivot do\n         //do-nothing\n      end while\n"+
                            "      if leftPointer >= rightPointer\n         break\n      else\n         swap leftPointer,rightPointer\n"+
                            "      end if\n   end while \n   swap leftPointer,right\n   return leftPointer\nend function\n",
                'Linear Search': "procedure linear_search (list, value)\n   for each item in the list\n      if match item == value\n"+
                                "         return the item's location\n      end if\n   end for\nend procedure",
                'Binary Search': "Procedure binary_search\n   A ← sorted array\n   n ← size of array   x ← value to be searched\n"+
                                "   Set lowerBound = 1\n   Set upperBound = n \n\n   while x not found\n      if upperBound < lowerBound \n"+
                                "         EXIT: x does not exists.\n      set midPoint = lowerBound + ( upperBound - lowerBound ) / 2\n"+
                                "      if A[midPoint] < x\n         set lowerBound = midPoint + 1\n      if A[midPoint] > x\n"+
                                "         set upperBound = midPoint - 1 \n      if A[midPoint] = x \n         EXIT: x found at location midPoint\n"+
                                "   end while\nend procedure",
                'A* algorithm': "let openList equal empty list of nodes\nlet closedList equal empty list of nodes\nput startNode on the openList (leave it's f at zero)\n"+
                                "while openList is not empty\n    let currentNode equal the node with the least f value\n"+
                                "    remove currentNode from the openList\n    add currentNode to the closedList\n"+
                                "    if currentNode is the goal\n        You've found the exit!\n    let children of the currentNode equal the adjacent nodes\n"+
                                "    for each child in the children\n        if child is in the closedList\n            continue to beginning of for loop\n"+
                                "        child.g = currentNode.g + distance b/w child and current\n        child.h = distance from child to end\n"+
                                "        child.f = child.g + child.h\n        if child.position is in the openList's nodes positions\n"+
                                "            if child.g is higher than the openList node's g\n                continue to beginning of for loop\n"+
                                "        add the child to the openList\n",
                'Dijsktra': "let openList equal empty list of nodes\nlet closedList equal empty list of nodes\n"+
                            "put startNode on the openList (leave it's f at zero)\nwhile openList is not empty\n"+
                            "    let currentNode equal the node with the least f value\n    remove currentNode from the openList\n"+
                            "    add currentNode to the closedList\n    if currentNode is the goal\n        You've found the exit!\n"+
                            "    let children of the currentNode equal the adjacent nodes\n    for each child in the children\n"+
                            "        if child is in the closedList\n            continue to beginning of for loop\n"+
                            "        child.g = currentNode.g + distance b/w child and current\n        child.h = distance from child to end\n"+
                            "        child.f = child.g + child.h\n        if child.position is in the openList's nodes positions\n"+
                            "            if child.g is higher than the openList node's g\n                continue to beginning of for loop"+
                            "\n        add the child to the openList",
                }



# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 380
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))

    window.update_idletasks()


# Randomly generate array
def generate():
    canvas.delete('all')
    global data,user_input

    data = []
    for i in range(0, 40):
        random_value = random.randint(1, 100)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])
    if algo_name_menu.get() == 'Linear Search':
         user_input = simpledialog.askstring(title="Linear Search",prompt="Element to be searched:")
    if algo_name_menu.get() == 'Binary Search':
         user_input = simpledialog.askstring(title="BInary Search",prompt="Element to be searched:")


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.5
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

def num_of_cmp(no_cmp):
    space.configure(text="NO. of comparission: "+str(no_cmp))

def sort():
    canvas.delete('all')
    global data
    timeTick = set_speed()
    os.environ['SDL_WINDOWID'] = str(canvas.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    if algo_name_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick,num_of_cmp)
    elif algo_name_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick,num_of_cmp)
    elif algo_name_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick,num_of_cmp)
    elif algo_name_menu.get() == 'A star':
        from algorithms import a_star
        WIDTH = 800 
        HEIGHT= 400
        global WIN
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        a_star.main(WIN,WIDTH)
    elif algo_name_menu.get() == 'Dijkstra':
        from algorithms import dijkstra
        WIDTH = 800 
        HEIGHT= 400
        global WIND
        WIND = pygame.display.set_mode((WIDTH, HEIGHT))
        dijkstra.main(WIND,WIDTH)
    elif algo_name_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick, num_of_cmp)
    elif algo_name_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick, num_of_cmp)
    elif algo_name_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    elif algo_name_menu.get() == 'Linear Search':
        linear_search(data, drawData, timeTick,num_of_cmp,user_input) 
    elif algo_name_menu.get() == 'Binary Search':
        binary_search(data, drawData, timeTick, user_input, num_of_cmp)    
    else:
        counting_sort(data, drawData, timeTick)

    
def clear_canvas():
    canvas.delete('all')

#converting algo list based on type
def set_algorithm(self):
    if algo_type_menu.get() == 'Sorting':
        print("Sorting")
        algo_name_menu['values']=sort_algo_list
        algo_name_menu.current(0)
    elif algo_type_menu.get() == 'Searching':
        print("Searching")
        algo_name_menu['values']=search_algo_list
        algo_name_menu.current(0)
    else:
        print("pathfinding")
        algo_name_menu['values']=path_algo_list
        algo_name_menu.current(0)
    

#setting information of algo
def set_info(self):
    if algo_name_menu.get() == 'Bubble Sort':
        label_algo_name.configure(text="Bubble Sort")
        complexity.configure(text=sort_information["Bubble Sort"])
        code_text.configure(text=pseudo_code["Bubble Sort"])

    elif algo_name_menu.get() == 'Insertion Sort':
        label_algo_name.configure(text="Insertion Sort")
        complexity.configure(text=sort_information['Insertion Sort'])
        code_text.configure(text=pseudo_code["Insertion Sort"])

    elif algo_name_menu.get() == 'Selection Sort':
        label_algo_name.configure(text="Selection Sort")
        complexity.configure(text=sort_information['Selection Sort'])
        code_text.configure(text=pseudo_code["Selection Sort"])

    elif algo_name_menu.get() == 'Merge Sort':
        label_algo_name.configure(text="Merge Sort")
        complexity.configure(text=sort_information['Merge Sort'])
        code_text.configure(text=pseudo_code["Merge Sort"],font=("comic sans ms", 10))

    elif algo_name_menu.get() == 'Quick Sort':
        label_algo_name.configure(text="Quick Sort")
        complexity.configure(text=sort_information['Quick Sort'])
        code_text.configure(text=pseudo_code["Quick Sort"])

    elif algo_name_menu.get() == 'Linear Search':
        label_algo_name.configure(text="Linear Search")
        complexity.configure(text=search_information['Linear Search'])
        code_text.configure(text=pseudo_code["Linear Search"])

    elif algo_name_menu.get() == 'Binary Search':
        label_algo_name.configure(text="Binary Search")
        complexity.configure(text=search_information['Binary Search'])
        code_text.configure(text=pseudo_code["Binary Search"])


    elif algo_name_menu.get() == 'A star':
        label_algo_name.configure(text="A star")
        code_text.configure(text=pseudo_code["A* algorithm"])

    else:
        label_algo_name.configure(text="Dijkstra")
        code_text.configure(text=pseudo_code["Dijsktra"])



# taking user input 
def userInput():
    canvas.delete('all')
    global data
    user_input = t1.get("1.0","end-1c")
    data = user_input.split(",")
    for i in range(0,len(data)):
        data[i] = int(data[i])

    drawData(data, [BLUE for x in range(len(data))])


### User interface ###
UI_frame = Frame(window, width= 900, height=300, bg="light salmon",relief="raised",bd=2,
                    highlightbackground=BLACK,highlightthickness=1)
UI_frame.grid(row=0, column=0, padx=20, pady=15,sticky=NW)

algo_type = Label(UI_frame, text="Algo Type: ", bg="light salmon", font=("Helvetica", 10,"bold"))
algo_type.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_type_menu = ttk.Combobox(UI_frame, textvariable=algorithm_type, values=algo_type_list)
algo_type_menu.grid(row=0, column=1, padx=5, pady=5)
algo_type_menu.bind('<<ComboboxSelected>>',set_algorithm)
algo_type_menu.current(0)

algo_name = Label(UI_frame, text="Algo Name: ", bg="light salmon", font=("Helvetica", 10,"bold"))
algo_name.grid(row=1, column=0, padx=10, pady=5, sticky=W)
algo_name_menu = ttk.Combobox(UI_frame, textvariable=sort_algorithm_name)
algo_name_menu.grid(row=1, column=1, padx=5, pady=5)
algo_name_menu.bind('<<ComboboxSelected>>',set_info)

l2 = Label(UI_frame, text="Sorting Speed: ", bg="light salmon", font=("Helvetica", 10,"bold"))
l2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=2, column=1, padx=5, pady=5)
speed_menu.current(0)

man_inp = Label(UI_frame, text="Manual Input: ", bg="light salmon", font=("Helvetica", 10,"bold"))
man_inp.grid(row=3,column=0,padx=5,pady=5)

t1 = Text(UI_frame,width=20, height=1)
t1.grid(row=3,column=1,padx=5,pady=5)

b4= Button(UI_frame, text="Generate Array", command= userInput, bg=LIGHT_GRAY)
b4.grid(row=3,column=2,padx=5,pady=5)

b3 = Button(UI_frame, text="Random Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=4, column=0, padx=5, pady=5)

b1 = Button(UI_frame, text="Start", command=sort, bg=LIGHT_GRAY)
b1.grid(row=4, column=1, padx=5, pady=5)

clr = Button(UI_frame, text="Clear", command=clear_canvas, bg=LIGHT_GRAY)
clr.grid(row=4, column=2, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg="pale goldenrod")
canvas.grid(row=0, column=0, padx=20,pady=30)

panel_1 = PanedWindow(bd=4,bg="blue",relief="raised",orient=VERTICAL,width=500,height=800)
panel_1.grid(row=0,column=1)

algo_info_canvas = Frame(width=300,height=280,bg="RoyalBlue3",bd=4)
panel_1.add(algo_info_canvas)

label_1 = Label(algo_info_canvas,text="Algo Name: ", bg="RoyalBlue3",fg="midnight blue",
            font=("comic sans ms", 13,"bold"))
label_1.grid(row=0, column=0, padx=10, pady=5)
label_algo_name = Label(algo_info_canvas, bg="RoyalBlue3",fg="midnight blue",
            font=("comic sans ms", 13,"bold"))
label_algo_name.grid(row=0, column=1, padx=10, pady=5)

complexity = Label(algo_info_canvas, bg="RoyalBlue3",fg="midnight blue",
            font=("comic sans ms", 13,"bold"))
complexity.grid(row=1, column=1, padx=10, pady=5)

space = Label(algo_info_canvas,bg="RoyalBlue3",text="NO. of Comparission: 0",fg="midnight blue",height=3,
            font=("comic sans ms", 13,"bold"))
space.grid(row=2,column=0, padx=10, pady=5)

space_1 = Label(algo_info_canvas,bg="RoyalBlue3",height=2)
space_1.grid(row=3, padx=10, pady=5)

sudo_code = Frame(width=330,height=200,bg="tomato",relief="sunken")
panel_1.add(sudo_code)

code_text = Label(sudo_code,bg="tomato",font=("comic sans ms", 12),justify=LEFT)
code_text.grid(row=0,column=0,pady=5)

window.mainloop()