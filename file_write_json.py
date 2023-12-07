import json

my_file = 'hello_out.json'
points_3D = [[3, 5, 2], [1, 2, 0], [3, 1, 1], [0, 0, 2], [4, 2, 3]]
# w - write
with open(my_file, 'w') as f:
    json.dump(points_3D, f)