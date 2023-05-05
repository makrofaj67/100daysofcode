import pandas

data = pandas.read_csv("100daysofcode/26/nato_phonetic_alphabet.csv")
print(data)

new_dict = {row.letter: row.code for index, row in data.iterrows()}
print(new_dict)
{"A": "Alfa", "B": "Bravo"}
name = input("neyi dönüştürmek istiyorsunuz").upper()
istenenlist = [new_dict[letter] for letter in name]
print(istenenlist)