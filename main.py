student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {word.letter: word.code for (letter, word) in nato_phonetic_alphabet.iterrows()}

user_inputs = input("Enter a word: ").upper()

phonetic_code_words = [nato_phonetic_dict[letter] for letter in user_inputs]
print(phonetic_code_words)
