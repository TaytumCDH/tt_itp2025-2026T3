orchard = [24,52,12,23,43,32,33,12,19,24,42,52,37,27,31,43,34,24]

basket = 0
truck = []
for x in orchard:
    while(x>0):
        print("There are "  + str(x) + " number of apples on the tree and " +str(basket) + " apples in the basket.")
        print("I pick 1 apple and put it in the basket.")
        x=x-1
        basket += 1
        print("There are "  + str(x) + " number of apples on the tree and " +str(basket) + " apples in the basket.")
    truck.append(basket)
    basket=0
    print(truck)