num_list = [(3, 5), (1, 2), (3, 1), (0, 0), (4, 2)]
x, y = num_list[1]
print(x, y)

#list_2D = [(3, 5, 2), (1, 2, 0), (3, 1, 1), (0, 0, 2), (4, 2, 3)]
#list_2D = ((3, 5, 2), (1, 2, 0), (3, 1, 1), (0, 0, 2), (4, 2, 3))
list_2D = [[3, 5, 2], [1, 2, 0], [3, 1, 1], [0, 0, 2], [4, 2, 3]]
for row in list_2D:
    print(row)

#TODO:
# 1. Create a list of sums of each row
row_sum = [ sum(row) for row in list_2D]
print(row_sum)
# 2. Sum all elements of the matrix
# 3. Create a list of sums of each column
col_list = [0, 0, 0]
for row in list_2D:
    for i in range(len(row)):
        col_list[i] += row[i]
print(col_list)
print('-------- ZIP -----------')

transposed_list_2D = list(zip(*list_2D))
print(transposed_list_2D)
row_sum = [ sum(row) for row in transposed_list_2D]
print(row_sum)


print('-------- NUMPY -----------')


import numpy as np
list_row = []
list_col = []

list_2D_transpose = np.asarray(list_2D).transpose()
for rows in list_2D_transpose:
    list_col.append(sum(rows))
print(list_col)

#print(sum(list_row))

# list_2D_transpose = []
# tmp = []
#
# for i in range(len(list_2D[0])):
#      tmp = []
#      tmp.append(list_2D[0][i])
#      list_2D_transpose.append(tmp)
#
# for i in range(1,len(list_2D)):
#      for j in range(len(list_2D[i])):
#          tmp = []
#          tmp = list_2D_transpose[j]
#          tmp.append(list_2D[i][j])
#          list_2D_transpose[j] = tmp
#
# for col in list_2D_transpose:
#     list_col.append(sum(col))
#print(list_col)


