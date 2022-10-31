#1. Create a greeting for your program.
welcome_message = "WELCOME TO THE PROGRAM - BAND NAME GENERATOR\n"
print(welcome_message)

#2. Ask the user for the city that they grew up in.
user_city = input("What city did you grew up in?:\n")

#3. Ask the user for the name of a pet.
user_pet_name = input("What the name of your pet?:\n")

#4. Combine the name of their city and pet and show them their band name.
band_name = user_city + " " + user_pet_name

print(f"Your band name can be the following: {band_name} !")

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end 