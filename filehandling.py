x = int(input("enter and width: "))
y = int(input("enter a height: "))

def full_pyramid(x, y):

    for i in range(0,y):
        if i == 0:
            print(" "+"*"*((y*2)+6))
        print("*   " + ' '*(y-i-1) + '*'*(2*i+1) +  ' '*(y-i-1) + "    *")

def arrowShaft(trunk):
    for i in range(y):
        print("*" + " "*(y+1) + " *"+ " "*(y+1) + "  *")


full_pyramid(x,y)
arrowShaft(x)
print(" "+"*"*((y*2)+6))