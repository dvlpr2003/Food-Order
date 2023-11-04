import time
from os import system
from process import food_Order
#initializing object for the food_Order class
obj = food_Order()
print("Welcome to our food ordering site!\nLoading your menu... ")
time.sleep(4)
system("clear")
print("Available items \n")
#calling Display function from the food_Order class
obj.Display_food_items()

order_list = input("Select your food items : ").split(" ")
system("clear")
final_order = [int(items) for items in order_list]
print("Selected food items ")
obj.Selected_food_items(final_order)
obj.Payment()





  