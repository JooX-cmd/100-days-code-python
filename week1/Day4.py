import random 
# num = random.randint(1,10000)
# print(num)

# print("Head")
# print("Tail")


# random_choice =  random.randint(0,1)
# if random_choice == 0 :
#     print("Heads")
# else:
#     print(random_choice)
#----------------------------------------------------------------------------------------------
#List 

#option 1 for choice  a random form list  



# friends = ["lalal", "111efefwef", "jpkrpjgr"]

# print(random.choice(friends))

# sec option 
# random_index = random.randint(0,2)
# print(friends[random_index])
#-----------------------------------------------------------------------------------------------------------

# frist try  - my self code 

# Rock , Paper, scissor Game

Rock = ''' 

#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
'''

Paper = ''' 

#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
'''

scissor = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
'''
# win 
# lose
# t3adol

choice  =[Rock,Paper,scissor]
choice_name = ["Rock","Paper","scissor"]
print("choice ")
print("Type 0 for Rock, 1 for Paper, 2 for Scissors")
user_choice = int(input("Enter ur choice"))
if user_choice < 0 or user_choice >2 :
       print("Invalid choice! You lose by default 😅")
else:
    
    
    print(choice[user_choice])
    computer_choice = random.randint(0 ,2 )


    print(choice[computer_choice])
    
    if user_choice == computer_choice:
        print("🤝 It's a tie! ")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("🎉 You win! ")
    else:
        print("💻 Computer wins! !")

































