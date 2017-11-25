string = str(input('Please enter the text for analysis: \n'))
my_list = string.split(" ")
result_list = [""]
for i in range(len(my_list)):
    if len(my_list[i]) > len(result_list[0]):
        result_list.clear()
        result_list.append(my_list[i])
    if len(my_list[i]) == len(result_list[0]):
        result_list.append(my_list[i])
del result_list[0]
print('The longest word(s) in the text is: ')
for element in result_list:
    print(element)
