string = str(input('Please enter the text for analysis: \n'))
count = 0

for element in string:
    if element == 'b':
        count += 1

print('Number of characters "b" in text is equal ' + str(count))
