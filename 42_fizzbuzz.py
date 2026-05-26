#Okay so this basically works by when if FIB is divisble by 3 it prints Fizz and if Fib is divisble by 5 then it prints Buzz and if the number is divisble by 15 then it prints FizzBuzz
for FIB in range(100):
# To change number of rounds then change the ranges number 
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