import plotly.express as px
import pandas as pd
points_2D = [(3, 5), (1, 2), (3, 1), (0, 0), (4, 2)]
df = pd.DataFrame(points_2D, columns=['x', 'y'])
#fig = px.scatter(df, x='x', y='y')
#fig.show()

#############################################
points_3D = [[3, 5, 2], [1, 2, 0], [3, 1, 1], [0, 0, 2], [4, 2, 3]]
df3d = pd.DataFrame(points_3D, columns=['x', 'y', 'z'])
fig = px.scatter_3d(df3d, x='x', y='y', z='z')
fig.show()
