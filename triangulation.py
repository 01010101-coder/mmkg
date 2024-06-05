import random
import matplotlib.pyplot as plt


def create_points(number=10, x=50):  # генерируем точки
    points = []
    for i in range(number):
        points.append([random.randint(-x, x), random.randint(-x, x)])
    return points


def plot_polygon(polygon, title="Полигон", line=True):  # выводим полигон
    if line:  # если нам нужны отрезки
        polygon.append(polygon[0])
        x, y = zip(*polygon)
        polygon.pop(-1)
        plt.plot(x, y, 'o-')
        plt.title(title)
        plt.show()
    else:  # если нам нужны только точки
        x, y = zip(*points)
        plt.scatter(x, y)
        plt.title(title)
        plt.show()


def orientation(p, q, r):  # проверяем ориентацию трех точек
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def is_polygon_simple(points):  # проверка на самопересекаемость полигона
    def do_lines_intersect(p1, p2, q1, q2):  # пересечение двух отрезков
        def on_segment(p, q, r):  # находится ли точка на отрезке
            if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
                return True
            return False  # находится ли точка на отрезке

        o1 = orientation(p1, p2, q1)
        o2 = orientation(p1, p2, q2)
        o3 = orientation(q1, q2, p1)
        o4 = orientation(q1, q2, p2)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and on_segment(p1, q1, p2):
            return True
        if o2 == 0 and on_segment(p1, q2, p2):
            return True
        if o3 == 0 and on_segment(q1, p1, q2):
            return True
        if o4 == 0 and on_segment(q1, p2, q2):
            return True

        return False

    n = len(points)
    if n < 3:
        return False

    for i in range(n):
        for j in range(i + 1, n):
            if j != (i + 1) % n and j != (i - 1 + n) % n:
                p1, p2 = points[i], points[(i + 1) % n]
                q1, q2 = points[j], points[(j + 1) % n]
                if do_lines_intersect(p1, p2, q1, q2):
                    return False
    return True


def jarvis_march(points):  # алгоритм Джарвиса для нахождения минимальной выпуклой оболочки
    n = len(points)

    hull = []

    l = min(range(n), key=lambda i: points[i])
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[q], points[i]) == 2:
                q = i
        p = q
        if p == l:
            break

    return hull


def construct_simple_polygon(points):  # главная функция
    if len(points) < 3:
        return points

    hull_points = jarvis_march(points)
    plot_polygon(hull_points, "Минимальная выпуклая оболочка")

    remaining_points = [p for p in points if p not in hull_points]

    for p in remaining_points:
        for i in range(len(hull_points)):
            new_polygon = hull_points[:i] + [p] + hull_points[i:]
            if is_polygon_simple(new_polygon):
                hull_points = new_polygon
                break

    return hull_points


points = create_points(20, 70)
plot_polygon(points, "Множество точек", False)
print(points)

simple_polygon = construct_simple_polygon(points)
print(simple_polygon)

plot_polygon(simple_polygon, "Самонепересекающийся полигон")
