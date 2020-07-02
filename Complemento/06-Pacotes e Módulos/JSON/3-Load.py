import json

student = {
    "Name": "Peter",
    "Roll_no": "0090014",
    "Grade": "A",
    "Age": 20
}

with open("data.json", "w") as write_file:
    json.dump(student, write_file)

with open("data.json", "r") as read_file:
    b = json.load(student, read_file)

print(b)
