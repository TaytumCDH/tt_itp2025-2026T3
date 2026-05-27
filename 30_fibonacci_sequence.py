fib = [0,1]
total_to_count = 10
total_range = list(range(total_to_count-2))
for num in total_range:
    new_num = fib[num] + fib[num+1]
    fib.append(new_num)
print(fib)

#1/1 - Formatting
#0/1 - Comments
#3/3 - Content