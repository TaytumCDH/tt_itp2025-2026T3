spam = list(range(100))

spam.sort(reverse = True)

for x in spam:
    if x == 0:
        print("None left!")
    else:
        print(str(x) +" bottles of pop on the wall, " + str(x) + " bottles of pop! Take one down, pass it around, " + str(x-1) + " bottles of pop on the wall!")

#1/1 - Formatting
#0/1 - Comments
#3/3 - Content