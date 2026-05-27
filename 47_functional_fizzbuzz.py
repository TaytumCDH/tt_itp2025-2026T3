#okay this is basicaly the workswhen you put in the code FizzBuzz() and put a number in the perentheses for how many rounds you want to play 
def FizzBuzz(X):
 for FIB in range(X+1):
    if FIB == 0:
        print("0")
    elif FIB % 15 == 0:
        print("FizzBuzz")
    elif FIB % 3 == 0:
        print("Fizz")
    elif FIB % 5 == 0:
        print("Buzz")
    else:
        print(FIB)
FizzBuzz(1000)

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content