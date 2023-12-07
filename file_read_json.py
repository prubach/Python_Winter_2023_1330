import json

my_file = 'hello_out.json'
# r - write
with open(my_file, 'r') as f:
    my_points = json.load(f)
    print(my_points)
    print(my_points[1][1])