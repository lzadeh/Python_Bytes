'''
Exercise 1: Temperature Conversion
Write a Python program that converts a temperature from Celsius to Fahrenheit. 
Prompt the user to input a temperature in Celsius and calculate 
the equivalent temperature in Fahrenheit using the formula: 
Fahrenheit = (Celsius * 9/5) + 32. 
'''

# Prompt the user to enter a temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula
fahrenheit = (celsius * 9/5) + 32

# Display the equivalent temperature in Fahrenheit
print(celsius, "degrees Celsius is equal to ", fahrenheit, " degrees Fahrenheit.")
##################################################################################
# End of first exercise
##################################################################################



'''
Exercise 2: Currency Converter
Create a program that converts an amount in US dollars to euros. 
Ask the user to input the amount in dollars and then calculate 
the equivalent amount in euros using an exchange rate (e.g., 1 dollar = 0.85 euros).
'''
# Ask the user to input the amount in dollars
dollars = float(input("Enter the amount in US dollars: "))

# Define the exchange rate
exchange_rate = 0.85  # 1 dollar = 0.85 euros

# Calculate the equivalent amount in euros
euros = dollars * exchange_rate

# Display the result
print(dollars, " US dollars is equivalent to ", euros, " euros.")
##################################################################################
# End of second exercise
##################################################################################


'''
Exercise 3: Grocery Shopping Budget
Assume you have a budget for grocery shopping. Write a program that allows the user 
to input the budget and the prices of three grocery items. 
Calculate and display the remaining budget after purchasing those items.
'''
# Get the budget from the user
budget = float(input("Enter your budget: $"))

# Get the prices of three grocery items
item1_price = float(input("Enter the price of item 1: $"))
item2_price = float(input("Enter the price of item 2: $"))
item3_price = float(input("Enter the price of item 3: $"))

# Calculate the total cost of the items
total_cost = item1_price + item2_price + item3_price

# Calculate the remaining budget
remaining_budget = budget - total_cost

# Check if the budget is sufficient
if remaining_budget >= 0:
    print(f"You have ${remaining_budget:.2f} left after purchasing the items.")
else:
    print(f"Sorry, you overspent your budget by ${abs(remaining_budget):.2f}.")
##################################################################################
# End of third exercise
##################################################################################


'''
Exercise 4: Area of a Triangle
Prompt the user to input the base and height of a triangle. 
Calculate and display the area of the triangle using 
the formula: Area = 0.5 * base * height.
'''
# Prompt the user for input
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Display the result
print(f"The area of the triangle with base {base} and height {height} is {area}.")
##################################################################################
# End of the fourth  exercise
##################################################################################


'''
Exercise 5: Travel Time Calculator
Imagine you're planning a road trip. Ask the user to input the distance in kilometers 
and the average speed in kilometers per hour. Calculate and display the estimated travel time in hours.
'''

# Get user input for distance and average speed
distance_km = float(input("Enter the distance in kilometers: "))
average_speed_kph = float(input("Enter the average speed in kilometers per hour: "))

# Calculate the estimated travel time in hours
travel_time_hours = distance_km / average_speed_kph

# Display the result
print(f"Estimated travel time: {travel_time_hours:.2f} hours")
##################################################################################
# End of the fifth exercise
##################################################################################