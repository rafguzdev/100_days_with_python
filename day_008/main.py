import pyfiglet
text = pyfiglet.figlet_format('cesar cipher')
print(text)
message = input('Type a word: ')
shift = int(input('Type the shift number: '))
decode = []
for letter in message:
    decode.append(chr(ord(letter)-shift))

print(''.join(decode))
