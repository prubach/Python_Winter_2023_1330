import matplotlib.pyplot as plt
points_2D = [(3, 5), (1, 2), (3, 1), (0, 0), (4, 2)]
xs = [i[0] for i in points_2D]
ys = [i[1] for i in points_2D]
print(xs)
print(ys)

plt.plot(xs, ys, 'o')
plt.xlabel('X axis')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('plot2D.png')
plt.show()

#############################################
points_3D = [[3, 5, 2], [1, 2, 0], [3, 1, 1], [0, 0, 2], [4, 2, 3]]
xs = [i[0] for i in points_3D]
ys = [i[1] for i in points_3D]
zs = [i[2] for i in points_3D]
