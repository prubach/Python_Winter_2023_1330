my_file = 'numbers.csv'

f = open(my_file, 'r')
lines = f.readlines()
i = 0
for line in lines:
    i += 1
    print(f'{i}: {line}', end='')

#TODO - read these numbers into a 2D list and then sum rows, cols and all