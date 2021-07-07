import pandas
data = pandas.read_csv('alphabet.csv')
word = input('Type a word: ')

for letter in word:
    for (idx, row) in data.iterrows():
        if row.letter == letter.upper():
            print(row.code)



# student_data_frame = pandas.DataFrame(students)
# print(student_data_frame)
# for (idx, row) in student_data_frame.iterrows():
#     print(row.student) 