

#simple

# print("welcome to the tip calculator!")

# clac = int(input("what was the total bill  "))
# tip_calc = int(input("How much tip whould like to give? "))
# print(int(clac) / int(tip_calc))

#like bro do this 

print("welcome to the tip calculator")
bill = float(input("what is ur total billl ?  $"))
tip = int(input("what percentage tip would you like to give ? 10% 20%"))
people = int(input("How meny pepole to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount  = round(bill_per_person, 2 )
print (f"Eech persone should pay : $ {final_amount}")