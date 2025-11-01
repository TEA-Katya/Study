import math
def distance(point1, point2):
    #Вычисляем расстояние между двумя точками в 3D пространстве
    return math.sqrt((point1[0] - point2[0])**2 +
                     (point1[1] - point2[1])**2 +
                     (point1[2] - point2[2])**2)

def find_closest_points(points):
    #Находим две точки с минимальным расстоянием друг от друга
    min_dist = float('inf')  # Инициализируем бесконечностью
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)): # чтобы не повторять сравнения
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (i, j)

    return closest_pair, min_dist

# координаты точек
X = (11, 6, 3)
Y = (8, 5, 7)
Z = (27, 12, 9)
T = (14, 11, 25)

points = [X, Y, Z, T]
print(f"Точки x,y,z,t: {points}")
(point_indices, min_distance) = find_closest_points(points)

print(f"Точки {point_indices[0]+1} и {point_indices[1]+1} находятся на минимальном расстоянии: {min_dista
