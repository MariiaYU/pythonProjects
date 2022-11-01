import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_name = input("What is your name?: ")

nato_user_name = [alphabet_dict[f"{letter.upper()}"] for letter in user_name if letter != " "]

print(nato_user_name)
