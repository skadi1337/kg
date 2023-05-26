import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаем координаты вершин каркасной модели буквы K
vertices = [
    [1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1, 1], [1, 2, 1, 1],
    [3, 1, 1, 1], [4, 1, 1, 1], [4, 2, 1, 1], [3, 2, 1, 1],
    [2, 1, 3, 1], [2, 2, 3, 1], [2, 1, 4, 1], [2, 2, 4, 1],
    [2, 2, 5, 1], [2, 1, 5, 1],
    [1, 1, 8, 1], [2, 1, 8, 1], [2, 2, 8, 1], [1, 2, 8, 1],
    [3, 1, 8, 1], [4, 1, 8, 1], [4, 2, 8, 1], [3, 2, 8, 1]
]

# Задаем индексы ребер каркасной модели буквы K
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [1, 8], [2, 9],
    [4, 8], [7, 9], [5, 10], [6, 11],
    [0, 14], [13, 15], [12, 16], [3, 17],
    [14, 15], [15, 16], [16, 17], [17, 14],
    [10, 19], [13, 18], [11, 20], [12, 21],
    [18, 19], [19, 20], [20, 21], [21, 18]
]


def m_scale(x, y, z):
    matrix = np.array([[x, 0, 0, 0],
                     [0, y, 0, 0],
                     [0, 0, z, 0],
                     [0, 0, 0, 1]])
    print(matrix)
    return matrix


def m_rotate_x(angle):
    cos_angle = np.cos(np.radians(angle))
    sin_angle = np.sin(np.radians(angle))
    matrix = np.array([[1, 0, 0, 0],
                       [0, cos_angle, -sin_angle, 0],
                       [0, sin_angle, cos_angle, 0],
                       [0, 0, 0, 1]])
    print(matrix)
    return matrix


def m_rotate_y(angle):
    cos_angle = np.cos(np.radians(angle))
    sin_angle = np.sin(np.radians(angle))
    matrix = np.array([[cos_angle, 0, sin_angle, 0],
                       [0, 1, 0, 0],
                       [-sin_angle, 0, cos_angle, 0],
                       [0, 0, 0, 1]])
    print(matrix)
    return matrix


def m_rotate_z(angle):
    cos_angle = np.cos(np.radians(angle))
    sin_angle = np.sin(np.radians(angle))
    matrix = np.array([[cos_angle, -sin_angle, 0, 0],
                       [sin_angle, cos_angle, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    print(matrix)
    return matrix


def m_move(x, y, z):
    matrix = np.array([[1, 0, 0, x],
                       [0, 1, 0, y],
                       [0, 0, 1, z],
                       [0, 0, 0, 1]])
    print(matrix)
    return matrix


def change_vertices(verts, matrix):
    return list(map(lambda vert: list(np.dot(np.array(vert), matrix)), verts))


# Создаем 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vertices = change_vertices(vertices, m_scale(1, 1, 1.5))
vertices = change_vertices(vertices, m_rotate_z(15))
vertices = change_vertices(vertices, m_move(1, 5, -5))

# Отрисовываем вершины и ребра
for edge in edges:
    vert1 = vertices[edge[0]]
    vert2 = vertices[edge[1]]
    ax.plot([vert1[0], vert2[0]], [vert1[1], vert2[1]], [vert1[2], vert2[2]], 'black')
    ax.plot([vert1[0], vert2[0]], [vert1[1], vert2[1]], [0, 0], 'red')
    ax.plot([vert1[0], vert2[0]], [0, 0], [vert1[2], vert2[2]], 'green')
    ax.plot([0, 0], [vert1[1], vert2[1]], [vert1[2], vert2[2]], 'purple')

# Настраиваем параметры отображения
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 11)

plt.show()
