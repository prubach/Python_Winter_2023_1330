import os.path

work_dir = os.getcwd()
print(f'Current working dir: {work_dir}')


#my_file = 'C:\\Users\prubac\Desktop\myfile.txt'
#my_file = 'C:/Users\prubac\Desktop\myfile.txt'
my_file = 'data/myfile.txt'
#my_file = 'C:/Users\prubac\PycharmProjects\Python_Winter_2023_1330/data/myfile.txt'

if os.path.exists(my_file):
    print(f'{my_file} found!')
else:
    print(f'{my_file} not found!!!')
    exit(100)

with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')