# number_of_hours = int(input("Enter number of working hours per month:"))
# wage_per_hour = float(input("Enter wage per hour:"))

# monthly_income = number_of_hours*wage_per_hour
# print("Monthly income is ", monthly_income)


base_price_per_sqft = 1500
value_per_bedroom = 10000

home_area_sqft = float(input("Enter home area in square feet:"))
number_of_bedrooms = int(input("Enter number of bedrooms:"))

total_value = home_area_sqft * base_price_per_sqft + number_of_bedrooms * value_per_bedroom

print("Total value of home is", total_value)

