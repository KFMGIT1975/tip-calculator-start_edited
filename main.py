#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
new_total_bill = float(total_bill)
tip = input("What percentage tip would like to give? 10, 12, or 15? ")
new_tip = int(tip)
total_bill_tip = new_total_bill + (new_total_bill * (new_tip / 100))
#print(total_bill_tip)
people = int(input("How many people to split the bll? "))
#bill_person = round(total_bill_tip / people, 2)
bill_person = total_bill_tip / people
final_amount = "{:.2f}".format(bill_person)
print(f"Each person should pay: ${final_amount}")
#print((type(new_total_bill)))
#print(type(new_tip))
