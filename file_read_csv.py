my_file = 'numbers.csv'

f = open(my_file, 'r')
lines = f.readlines()
i = 0
for line in lines:
    i += 1
    print(f'{i}: {line}', end='')

#TODO - read these numbers into a 2D list and then sum rows, cols and all

a = []
for line in lines:
    tmp = line.replace('\n','').split(sep=';')
    tmp = [int(x) for x in tmp]
    a.append(tmp)

print(a)

list_row = []
list_col = [0 for i in range(len(a[0]))]

for row in a:
    list_row.append(sum(row))

print(list_row)
print(sum(list_row))

for row in a:
    for i in range(len(row)):
        list_col[i] += row[i]

print(list_col)