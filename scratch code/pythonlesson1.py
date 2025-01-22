from math import*
from random import*

# functions
# RadToDegree
def RadToDegree(Rad):
    return Rad * 180 / pi

# Add2Vectors
def Add2Vectors(V1, V2):
    sum = []
    for i in range (3):
        sum.append(V1[i] + V2[i])
    return sum

# Quadtric Equation
def quadratic(a, b, c):
    if (b**2-4*a*c > 0):
        nbr1 = (-1*b)/(2*a)
        plusMinus = "+/-"
        nbr2 = ((b**2 - 4*a*c)**0.5)/(2*a)
    elif (b**2 - 4*a*c == 0):
        nbr1 = (-1*b)/(2*a)
        plusMinus = "+/-"
        nbr2 = 0
    else:
        nbr1 = (-1*b)/(2*a)
        plusMinus = "+/- i*"
        nbr2 = ((-1*(b**2 - 4*a*c))**0.5)/(2*a)
    return [nbr1, plusMinus, nbr2]

# List100
def List100():
    numbers = []
    for i in range (1, 101):
        numbers.append(i)
    return numbers

# ConsecSum
def ConsecSum():
    num = int(input('Enter a number: '))
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

# Leibnitz
def leibnitz(n):
    num = 1.0
    value = 0.0
    for i in range (1, n+1):
        if (i % 2 == 1):
            value += num**(-1)
        else:
            value -= num**(-1)
        num += 2
        
    return value*4 
        
# Secret
def Secret():
    rand = int(random()*1000)
    correct = False
    while (correct == False):
        num = int(input('Guess a number: '))
        if num > rand:
            print("Too High!")
        elif num < rand:
            print ("Too Low!")
        else:
            print ("Right!")
            correct = True
    
# Prime
def Prime(n):
    nums = [1, 2, 3]
    for i in range(4, n+1):
        while i %j != 0 and j < i**.5:
            
        
        

###Test Code
###Test RadToDegree
##print(RadToDegree(pi/4))
##
### Test Add2Vectors
##vector1 = [1,4,5]
##vector2 = [3,6,-3]
##print(Add2Vectors(vector1, vector2))
##
### Test Quadratic
##print(quadratic(6,2,18))
##
### Test List100
##print(List100())
##
### Test ConsecSum
##print(ConsecSum())
##
### Test Leibnitz
##print(leibnitz(100))

### Test Secret
##Secret()
