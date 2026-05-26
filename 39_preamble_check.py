# this checks for the words in this list then says hey i found the thing and names it or say i didnt and names it.
preamble = "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."
Check = ["Posterity","Secure","secure","ide for the co", "USB Drive", "domestic Tranquility", "Piano", "ice"]
for X in Check:
    if X in preamble:
        print("I found the string " + str(X) + " in the preamble")
    else: 
        print("I cannot find the string " + str(X) + " in the preamble")

