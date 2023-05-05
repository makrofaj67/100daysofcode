import random


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newlist = [n + 1 for n in list]

#print(newlist)

name = "Angela"

list = [letter for letter in name]

#print(list)

#print([n * 2 for n in range(1, 5)])

students = ["Angela", "James", "Lily", "Pam", "Sandra"]
scores = [56, 76, 98, 100, 99]

zipped = {student: score for student, score in zip(students, scores)}
print(zipped)

new_dict = {student: random.randint(1, 100) for student in students}
#print(new_dict)

#new_key: new_value for dict.Items() if test

#print(new_dict.items())

#new_dict.items()


new_dict2 = {key: value for key, value in new_dict.items() if value > 60}
print(new_dict2)
