#The toppings that available to go on a pizza
toppings = ["Grilled Chicken", "Pepperoni", "Beef", "Spicy Italian Sausage", "Bacon", "Sausage", "Canadian Bacon", "Mushrooms", "Green Olives", "Roma Tomatoes", "Pineapple", "Onions", "Black Olives", "Jalapeno Peppers", "Banana Peppers", "Green Peppers"]

#The pizza requests
first_pizza = ["Sausage", "Pepperoni", "Onions", "Green Peppers"]
second_pizza = ["Spicy Italian Sausage", "Skittles", "Pork Chops", "Mushrooms", "Brownies"]
third_pizza = ["Canadian Bacon", "Jalapeño Peppers, but not the gross pickled kind, because those give me a stomachache", "Grilled Onions","Pineapple"]
print("Order recieved!")
#This works by seeing the pizza requests toppings are on themenu and if not it say no i cannot be added then it cooks the pizza and then tells you ur pizza with the toppings that are allowed 
for X in second_pizza:
    #to change the order change second pizza to any request you want in for all to change your order
    if X in toppings:
        print("yes " + str(X) + " Can be added to the pizza.")
    else:
        print("No " + str(X) + " Cannot be added to the pizza")
for X in toppings:
    if X in second_pizza:
         print("Adding " + str(X) + " to the pizza...")
print("Baking has started..............")
print("Baking has finished with the toppings:")
for X in toppings:
    if X in second_pizza:
         print(X)

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content