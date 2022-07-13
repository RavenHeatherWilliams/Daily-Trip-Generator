from cProfile import run
from pydoc import describe
import random
from select import select
from tkinter import N, Y

welcome_script = 'Welcome to Day Trip Generator! We are here to help you vacation with ease!'
print(welcome_script)

destinations_list = ["New Orleans", "San Diego", "Washington D.C", "Orlando", "New York", "Staten Island"]

def random_destination_picker(destinations_list):
      random_destination_picker = random.choice("++")
      random_destination= random.choice(destinations_list)
      return random_destination

# print(random.choice(destinations_list))

def user_destinations_confirmation(destinations_list):
    user_confirmed =(False)
    while user_confirmed == (False):
        random_destination = random_destination_picker(destinations_list)
        user_input = input(f'Would you like to visit {random_destination} as your selected destination? y/n')
        if user_input == "y":
            print(f'Wonderful selection! {random_destination} is beautiful!')
            return random_destination
        elif user_input == "n":
            print(f' No worries! We have other options!')
        
   

# print(user_destinations_confirmation(destinations_list))

restaurant_list = ["Cafe DuMonde", "San Diego Crab House", "Uncaged Chefs", "Socco Restaurant", "Quality Bistro", "Patrizia's of Staten Island"]

def random_restaurant_picker(restaurant_list):
      random_restaurant_picker = random.choice("++")
      random_restaurant= random.choice(restaurant_list)
      return random_restaurant

def user_restaurant_confirmation(restaurant_list):
    user_confirmed =(False)
    while user_confirmed == (False):
        random_restaurant = random_restaurant_picker(restaurant_list)
        user_input = input(f'Hey foodie? How does {random_restaurant} sound? y/n')
        if user_input == "y":
            print(f'Good taste! {random_restaurant} comes highly recommended!')
            return random_restaurant

        elif user_input == "n":
            print(f' Variety is our specialty! Let us find something else!')
            

# print(user_restaurant_confirmation(restaurant_list))

transportation_list = ["Plane", "Train", "Car", "Boat", "Private Jet", "Bus"]

def random_transportation_picker(transportation_list):
      random_transportation_picker = random.choice("++")
      random_transportation= random.choice(transportation_list)
      return random_transportation


def user_transportation_confirmation(transportation_list):
    user_confirmed =(False)
    while user_confirmed == (False):
        random_transportation = random_transportation_picker(transportation_list)
        user_input = input(f'Getting ready for take off! Would you like to arrive by {random_transportation}?  y/n')
        if user_input == "y":
            print(f'One {random_transportation} coming right up!')
            return random_transportation

        elif user_input == "n":
            print(f' Decisions Decisions!')
            
# this works better if we want to print the value but we need to use the value again later
# confirmed_transportation is catching the return value of the function
# confirmed_transportation = user_transportation_confirmation(transportation_list)
# print(confirmed_transportation)

# this works great if we ONLY want to print the value and never use it again
# print(user_transportation_confirmation(transportation_list))

entertainment_list = ["Zoo", "Aquarium", "City Tour", "Whiskey Tasting", "ATV Excursion", "Concert"]

def random_entertainment_picker(entertainment_list):
      random_entertainment_picker = random.choice("++")
      random_entertainment= random.choice(entertainment_list)
      return random_entertainment

def user_entertainment_confirmation(entertainment_list):
    user_confirmed =(False)
    while user_confirmed == (False):
        random_entertainment = random_entertainment_picker(entertainment_list)
        user_input = input(f'Would you like to experience {random_entertainment} during the trip? y/n')
        if user_input == "y":
            print(f'{random_entertainment} is a perfect experience!')
            return random_entertainment

        elif user_input == "n":
            print(f'Rest assured! We have options for you!')
            

# print(user_entertainment_confirmation(entertainment_list))

def controller():
    destination_selection = user_destinations_confirmation(destinations_list)
    restaurant_selection_two = user_restaurant_confirmation(restaurant_list)
    transportation_selection_three = user_transportation_confirmation(transportation_list)
    entertainment_selection_four = user_entertainment_confirmation(entertainment_list)
    print (f'Thank you for choosing {destination_selection} and {restaurant_selection_two} and {transportation_selection_three} and {entertainment_selection_four}')

controller()

