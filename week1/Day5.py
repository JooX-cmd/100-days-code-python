import random
#For loop  
fruit = ["apple","lalalal", "babababab"] # if u print this u print it 3 times like this bec  u have 3 items in ur list
for lalalalllll in fruit:
    print(lalalalllll)
    print(lalalalllll + "  pie")

#-----------------------------------------------------------------


student_score = [150, 51, 5, 56, 56, 5, 56, 55, 588, 559, 660, 661, 624, 613, 64, 65, 6, 67, 68, 69, 70, 1, 72, 7, 74, 75, 76, 77, 78, 79, 80, 543, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
total_exam_score = sum(student_score) # builtin function
total  = 0 
for i  in student_score: # to understand for loop
    total += i
print(total)
#-------------------------------------------------------------------
student_score = [10000000000, 51, 5, 56, 56, 5, 56, 55, 588, 559, 660, 661, 624, 613, 64, 65, 6, 67, 68, 69, 70, 1, 72, 7, 74, 75, 76, 77, 78, 79, 80, 543, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#print(max(student_score)) # get max number 
# get max number for the list using loop
max_value = 0
number = 0
for i in range(len(student_score)):
   if  student_score[i] > max_value:
       max_value = student_score[i] # Get the ELEMENT, not the list  i got error here when  i use .index(i) value error  ?CRASH! 💀
       number = i
#print( max_value , student_score,number) 
print(f"Max value: {max_value}, Index: {number}")
#--------------------------------------------------------------------
# sec try
student_score = [150, 51, 5, 56, 56, 5, 56, 55, 588, 559, 660, 661, 624, 613, 64, 65, 6, 67, 68, 69, 70, 1, 72, 7, 74, 75, 76, 77, 78, 79, 80, 543, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

max_value = student_score[0] # to start from index 0 
max_index = 0

for index, value in enumerate(student_score):  #enumerate() gives us both index and value at the same time - very Pythonic! 🐍
    if value > max_value:
        max_value = value
        max_index = index

print(f"Max value: {max_value}, Index: {max_index}")
#------------------------------------------------------------------------------

student_score = [150, 51, 5, 56, 56, 5, 56, 55, 588, 559, 660, 661, 624, 613, 64, 65, 6, 67, 68, 69, 70, 1, 72, 7, 74, 75, 76, 77, 78, 79, 80, 543, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# Initialize max_score to 0
# We start with 0 as our baseline for comparison
max_score = 0 

# Loop through each score in the list
# First iteration: i = 150, 150 > 0? Yes, so max_score = 150
# Second iteration: i = 51, 51 > 150? No, keep max_score = 150
# Continue until we check all scores
for i in student_score:
    if i > max_score:
        max_score = i

print(f"The maximum score is: {max_score}")
#--------------------------------------------------------------------------

# FizzBuzz 

#- Your program should print each number from 1 to 100 in turn and include number 100.
#
#But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

#----------------------------------------------------------------------------------
#  password generator


lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
extended_symbols = '§±¡TM£¢∞¶•ao–≠œ∑ ́®† ̈ˆøπ"'

print("Welcome to the Password Generator")

lowercase_count = int(input("How many lowercase letters would you like in your password? "))
uppercase_count = int(input("How many uppercase letters would you like in your password? "))
digits_count = int(input("How many digits would you like in your password? "))
symbols_count = int(input("How many symbols would you like in your password? "))
extended_symbols_count = int(input("How many extended symbols would you like in your password? "))

pass_lowercase = ""
pass_uppercase = ""
pass_digits = ""
pass_symbols = ""
pass_extended_symbols = ""

for i in range(lowercase_count):
    random_lowercase = random.randint(0, 25)  
    pass_lowercase += lowercase[random_lowercase]

for i in range(uppercase_count):
    random_uppercase = random.randint(0, 25)  # Random index for uppercase letters
    pass_uppercase += uppercase[random_uppercase]

for i in range(digits_count):
    random_digits = random.randint(0, 9)  
    pass_digits += digits[random_digits]

for i in range(symbols_count):
    random_symbols = random.randint(0, len(symbols) - 1)  
    pass_symbols += symbols[random_symbols]

for i in range(extended_symbols_count):
    random_extended_symbols = random.randint(0, len(extended_symbols) - 1) 
    pass_extended_symbols += extended_symbols[random_extended_symbols]

pass_total = pass_lowercase + pass_uppercase + pass_digits + pass_symbols + pass_extended_symbols

# Shuffle the combined password random
pass_total_list = list(pass_total)
random.shuffle(pass_total_list)

# Join the shuffled list into a final password string
password = ''.join(pass_total_list)

# Output the generated password
print(f"Your password is: {password}")
