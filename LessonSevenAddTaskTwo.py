word_one = str(input('Please enter the first word: \n'))
word_two = str(input('Please enter the second word: \n'))

size_one = len(word_one)
size_two = len(word_two)

if size_one > size_two:
    word_one, word_two = word_two, word_one
    size_one, size_two = size_two, size_one

current_line = range(size_one + 1)
for i in range(1, size_two + 1):
    previous_line, current_line = current_line, [i] + [0] * size_one
    for j in range(1, size_one + 1):
        add, delete, change = previous_line[j] + 1, current_line[j - 1] + 1, previous_line[j - 1]
        if word_one[j - 1] != word_two[i - 1]:
            change += 1
        current_line[j] = min(add, delete, change)

print('Calculates the Levenshtein distance is ' + str(current_line[size_one]))
