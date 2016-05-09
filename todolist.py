import sys

itemnumber =

userinput = input ("Please specify a command [list, add, mark, archive]: ")

if userinput == "list":
    todolist = open ("todolist.txt" , "r")
    print (todolist.read())

elif userinput == "add":
    newitem = input ("Add an item: ")
    todolist = open ("todolist.txt" , "a+")
    todolist.writelines (str(itemnumber) + " [ ] " + (newitem) + "\n")

elif userinput == "mark":
    markitem = input ("Which one you want to mark as completed? ")

#elif userinput == "archive":

else:
    print ("Invalid input.")
