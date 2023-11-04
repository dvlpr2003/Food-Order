from available_food.food_data import Available_food
from pytz import timezone 
from datetime import datetime
import time
from os import system
class food_Order():
  def __init__(self):
    self.session = [
      item for item in Available_food.keys()
    ]
    self.morning_items = [
      item for item in Available_food[self.session[0]][0].keys()
    ]
    self.lunch_items = [
      item for item in Available_food[self.session[1]][0].keys()
    ]
    self.dinner_items = [
      item for item in Available_food[self.session[2]][0].keys()
    ]
    self.ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H')
    self.time_now = int(self.ind_time)
    self.cost_count = []
  def Display_food_items (self):

    if self.time_now < 11:
      for _ in range(len(self.morning_items)):
        print(f"{_+1}.{self.morning_items[_]}")
    elif self.time_now <16 :
      for _ in range(len(self.lunch_items)):
        print(f"{_+1}.{self.lunch_items[_]}")
    else :
      for _ in range(len(self.dinner_items)):
        print(f"{_+1}.{self.dinner_items[_]}")


  def Selected_food_items(self,selected_items):
    selected_items = selected_items
    if self.time_now < 11:
      for _ in selected_items:
        rupee = Available_food['Break fast'][0][self.morning_items[_-1]]['price']
        self.cost_count.append(rupee)
        print(f"{_}.{self.morning_items[_-1]} ₹{rupee}")
    elif self.time_now <16 :
      for _ in selected_items:
        rupee = Available_food['Lunch'][0][self.lunch_items[_-1]]['price']
        self.cost_count.append(rupee)
        print(f"{_}.{self.lunch_items[_-1]} ₹{rupee}")
    else :
      for _ in selected_items:
        rupee = Available_food['Dinner'][0][self.dinner_items[_-1]]['price']
        self.cost_count.append(rupee)
        print(f"{_}.{self.dinner_items[_-1]} ₹{rupee}")

  def Payment(self):
      total = 0
      for _ in self.cost_count:
        total = total + _
      print(f"Total price ₹{total}")
      get_confirmation = input("Do you want to checkout your food item (y/n): ")
      if get_confirmation == "y" or get_confirmation == "Y":
        system("clear")
        print(f"Total price ₹{total}")


        creditcard_number = input("Enter your Credit card number : ")
        cvv_number = input("Enter your CVV : ")
        system("clear")
        print("Processing ... ")
        time.sleep(5)
        system("clear")
        print("Payment Successful.")
        time.sleep(3)
        system("clear")
      if self.time_now < 11:
        print("     Enjoy your break fast...!")
      elif self.time_now <16 :
        print("     Enjoy your Lunch...!")
      else :
        print("     Enjoy your dinner...!")

        







      
      

