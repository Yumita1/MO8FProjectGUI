#To create a program for shopping list with option to add and delete shopping items

from tkinter import *

def createList(grocery):
    for elem in grocery:
        theList.insert(END,elem[0] + "-" + str(elem[1]))

def listIndex(grocery, item):
    index = -1
    for i in range(len(grocery)):
        if grocery [i][0] == item:
            index = i
        return index

def addList(grocery, item, index):
    if index == -1:
        grocery.append([item,1])
    else:
        grocery[index][1] += quantity.get()

def removeList(grocery, index):
    del(grocery[index])

def add():
    index = listIndex(grocery, item.get())
    addList(grocery, item.get(), index)
    if index >=0:
        theList.delete(index)
        theList.insert(index,grocery[index][0] + "-" + str(grocery[index][1]))
    else:
        theList.insert(END, item.get() + "-" + str(quantity.get()))

def remove():
    index = theList.index(ACTIVE)
    print(index)
    removeList(grocery, index)
    theList.delete(index)

grocery = [["rice", 1], ["ribeye", 2], ["coffee", 1], ["toothpaste", 1], ["milk", 1]]

window = Tk()
window.title("Grocery List")
#Added some foreground, background, width, height parameters
theList = Listbox(window, selectmode=MULTIPLE, foreground="green", background="yellow", width=42, height=25)
theList.grid(row=0, column=0, columnspan=15,sticky=E)

createList(grocery)

item=StringVar()
quantity=IntVar()

quantity.set(1)

Label(window, text="Item:", foreground="white", background="blue", width=8, height=2).grid(row=1, column=0)
Entry(window, textvariable=item).grid(row=1, column=1, sticky=W)

Label(window, text="Quantity:", foreground="white", background="purple",width=8, height=2).grid(row=2, column=0)
Entry(window, textvariable=quantity).grid(row=2, column=1 ,sticky=W)

Button(window, text="Add", foreground="white", background="green",width=8, height=2,command=add).grid(row=3, column=0)
Button(window, text="Remove", foreground="white", background="red",width=8, height=2, command=remove).grid(row=4, column=0)

window.mainloop()




            


            
