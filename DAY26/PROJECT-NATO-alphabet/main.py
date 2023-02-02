import pandas as pd

student_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

#print(student_data_frame)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# phonetic dictionary
nato_phonetic_dict = {row.letter:row.code for (index, row) in student_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("enter a word to get phonetic code: ").upper()
output = [nato_phonetic_dict[letter] for letter in user_input]
print(output)