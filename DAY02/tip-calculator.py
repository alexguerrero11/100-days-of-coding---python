#### Initial Problem
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150/5) + 1.12(150)/5

# User inputs of bill information, tip information, and amount of people 
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15 or 20? "))
total_people = int(input("How many people to split the bill? "))

# Calculation to split bill equally among all parties with tip included
tip_amount = total_bill * (tip_percentage/100)
total = total_bill + tip_amount
personal_total = total / total_people

# Round each person bill to 2 decimals
personal_total_round = round(personal_total,2)
personal_total_round = "{:.2f}".format(personal_total) #float turned into a string due to format

# Set variable equal to message
# Print variable
message = f"Each person should pay: ${personal_total_round}"
print(message)

#### EXAMPLE OUTPUT
# If total bill is $124.56, with a 12% tip, and 7 people to divide bill eqaully. 
# Each person should pay: $19.93