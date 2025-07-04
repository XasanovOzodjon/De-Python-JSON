
import json

with open('students.json', 'r') as file:
    students = json.load(file)

students.sort(key=lambda x: x['score'], reverse=True)

with open('rating.json', 'w') as file:
    json.dump(students, file, indent=4)
