# make a library of the students
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack-Russell"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},

]

# loop through each and print the information of every student
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")