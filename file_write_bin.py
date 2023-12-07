import _pickle

my_file = 'hello_out.dat'
points_3D = [[3, 5, 2], [1, 2, 0], [3, 1, 1], [0, 0, 2], [4, 2, 3]]
# wb - write binary
with open(my_file, 'wb') as f:
    _pickle.dump(points_3D, f)