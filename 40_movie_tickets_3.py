#This now checks how old they are if they are under 13 their ticket costs 8$ if older than 13 then it costs 12$ if 65 or older then it costs ten. if its tuesday then 2$ off!

age = '65'
is_Tuesday=True 
if is_Tuesday and age < '13':
    print('your ticket costs $6')
elif is_Tuesday and age >= '65':
    print('your ticket costs $8')
elif is_Tuesday and age >= '13':
    print('your ticket costs $10')
elif age < '13':
    print('your ticket costs $8')
elif age >= '65':
    print('your ticket costs $10')
elif age >= '13':
    print('your ticket costs $12')

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content
