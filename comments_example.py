# bill amount is the cost of the food.
bill_amount = float(input("Enter the bill amount:"))

tip_percent = int(input("Enter the tip percent:")) # tip precent is the precent of tip that user want to pay.

if tip_percent > 10:
    print("The tip percent is higher than 10 percent.")
    tip_percent = int(input("Please enter the tip percent lower than 10:")) 


'''
The total payable amount will be calculated by
adding the tip with the bill amount.
'''
total_amount = bill_amount + (bill_amount * tip_percent / 100)

print("The total bill amount is: ", total_amount)
