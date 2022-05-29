import random
name= ['Cyd', 'Rowan', 'Chief', 'Ione', 'Bertha', 'Goldie', 'Annalise', 'Jambette', 'Raymond', 'Sasha']
moving = random.choice(name)

x = input("Is someone staying at the campsite? ")
x = x.lower()
if x == "yes":
   camper = input("Who is staying at the campsite? ")
   camper = camper.capitalize()
   y = input("is " + camper + " moving in? ")
   y = y.lower()
   if y == "yes":
      print(moving + " is moving out")
   if y == "no":
      print(camper + " is not moving in")   

if x == "no":
   print("The campsite is empty")