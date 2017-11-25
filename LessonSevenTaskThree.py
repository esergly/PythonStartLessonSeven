string = str(input('Please enter the text for analysis: \n'))
sum = 0

for element in string:
    sum = sum + ord(element)
print(str(sum))
