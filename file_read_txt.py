my_file = 'hello.txt'

f = open(my_file, 'r')
lines = f.readlines()
i = 0
for line in lines:
    i += 1
    print(f'{i}: {line}', end='')