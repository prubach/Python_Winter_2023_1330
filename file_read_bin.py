import _pickle

my_file = 'hello_out.dat'
# rb - write binary
with open(my_file, 'rb') as f:
    my_points = _pickle.load(f)
    print(my_points)
    print(my_points[1][1])