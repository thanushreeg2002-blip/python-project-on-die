import random
print("dice rolling game")
while True:
   roll=random.randint(1,6)
   print("you rolled:",roll)
   choice = input("roll again? (yes/no):")
   if choice.lower() !="yes":
      break