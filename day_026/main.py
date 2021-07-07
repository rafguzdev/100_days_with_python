# list comprehension
with open('file1.txt') as reader:
    fnum1 = reader.readlines()

with open('file2.txt') as reader:
    fnum2 = reader.readlines()

new = [num.strip() for num in fnum1 if num in fnum2]
print(new)

# dictionary comprehension 1
import random
names = ['Alex', 'Beth', 'Rafal', 'Ada', 'Wojciech', 'Tomasz']
names_dict = {name:random.randint(1,100) for name in names}
print(names_dict)
passed = { name:val for name, val in names_dict.items() if val > 60 }
print(passed)

# dictionary comprehension 2
sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
new_dict = {word:len(word) for word in sentence.split()}
print(new_dict)

# dictionary comprehension 3
temp_c = { 'Monday': 12, 'Tuesday': 14, 'Wednesday': 14, 'Thursday': 21 }
temp_f = {day:(temp*9/5)+32 for (day, temp) in temp_c.items()}
print(temp_f)

# dictionary comprehension 4 pandas
import pandas
students = {
    'student': ['Ada', 'Rafal'],
    'score': [100, 90]
}
student_data_frame = pandas.DataFrame(students)
print(student_data_frame)
for (idx, row) in student_data_frame.iterrows():
    print(row.student) 