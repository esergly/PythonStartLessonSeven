name = str(input('Please enter the name: \n'))
size = len(name)
for i in range(size):
    if i == 0 and (ord(name[i]) < 65 or ord(name[i]) > 90):
        print('Incorrect first symbol in the name')
    elif i > 0 and (ord(name[i]) < 97 or ord(name[i]) > 122):
        print('The symbol "' + name[i] + '" is incorrect in the name')
