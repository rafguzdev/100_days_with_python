# load names
names = []
with open('Input/Names/invited_names.txt') as reader:
    for line in reader.readlines():
        names.append(line.strip())

# load starting letter
letter = ''
with open('Input/Letters/starting_letter.docx') as reader:
    # for line in reader.readlines():
    letter = reader.readlines()

if len(names) > 0 and len(letter) > 0:
    for name in names:
        line = f'Dear {name},'
        with open(f'Output/letter_for_{name}.docx', 'w') as f:
            letter[0] = line
            f.writelines(letter)