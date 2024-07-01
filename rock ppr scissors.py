import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
arr=[rock, paper, scissors]
print(f"Your choice is\n{arr[choice]}")
r=random.randint(0,2)
print(f"Computer chose\n{arr[r]}")
if(choice==2 and r==0) or (choice==1 and r==2) or (choice==1 and r==3) or (choice==0 and r==1):
    print("You lose!")
elif(choice==r):
    print("You're tied!")
elif(choice==2 and r==1) or (choice==0 and choice==2):
    print("You win!")
else:
    print("You lose!")