my_file = 'hello_out.txt'

# f = open(my_file, 'w')
# f.write('1st line of output')
# f.write('2nd line of output')
# f.flush()
# f.close()

# w - overwrite content
# a - append to a file
with open(my_file, 'a') as f:
    f.write('1st line of output\n')
    f.write('2nd line of output\n')