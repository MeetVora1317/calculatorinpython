import re

print(" our calculator")
print("Type 'quit' to exit\n")
previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the equation")
    else:
        equation = input(str(previous))
    equation = input("Enter equation: ")
    if equation == 'quit':
        run = False
        print("thank you")
    else:
        equation=re.sub('[a-zA-z,.:()""]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)
        print("you answer is",previous)

while run:
    performMath()
