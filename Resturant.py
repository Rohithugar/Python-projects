menu = {
    'Pizza' : 180,
    'Pasta' : 150,
    'Burger' : 120,
    'Salad' : 140,
    'Coffee' : 100,
    'Milk shake' : 120
}

print("Welcom to python restro")
print("Pizza : Rs 180\n, Pasta : Rs 150\n, Burger : Rs 120\n, Salad : Rs 140\n, Coffee : Rs 100\n,Milk shake : Rs 120")

order_total = 0

item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered iteam {item_1} is not avaialable yet!")

another_order = input("Do you want add another item? (Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter your second item = ")
    if item_2 in menu:
         order_total += menu[item_2]
         print(f" Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not avaialable!")

print(f"The total amount of the item to pay is : {order_total}")    







        
             