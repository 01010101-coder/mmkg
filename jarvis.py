points = [(-6, 6, 1), (4, 4, 2), (2, 8, 3), (-6, -6, 4), (2, 7, 5), (1, -9, 6), (7, -9, 7)]
old_points = points.copy()
points = sorted(points, key=lambda point: (point[1], point[0]))

answer = []

def vector(point1, point2):
    return (point2[0] - point1[0], point2[1] - point1[1])
def opredelitel(point1, point2):
    result = 0
    opredelitel = (point1[0] * point2[1]) - (point1[1] * point2[0])
    if opredelitel > 0:
        result = 1
    elif opredelitel < 0:
        result = -1
    else:
        result = 0

    return result

def perebor(points, answer):
    now_point = ()
    for i in range(len(points)):
        if points[i][0] != answer[-1][0] and points[i][1] != answer[-1][1]:
            now_point = points[i]
            break

    print(f"Считаем для ребра {answer[-1]} и {now_point}")
    for i in range(len(points)):
        now_vector = vector(answer[-1], now_point)
        if points[i][0] != answer[-1][0] or points[i][1] != answer[-1][1]:
            next_vector = vector(answer[-1], points[i])
            print(f"Считаем sign({now_vector}, {next_vector}) = {opredelitel(now_vector, next_vector)}")
            if opredelitel(now_vector, next_vector) == -1:
                print(f"sign = -1")
                now_point = points[i]
                print(f"Считаем для ребра {answer[-1]} и {now_point}")

    print(f"Остается точка: {now_point}")
    if now_point == answer[0]:
        return now_point, 0

    return now_point, 1

main_point = points[0]
answer.append(main_point)
print(f"Крайняя точка: {main_point}")
flag = 1
while flag:
    new_point, flag = perebor(points, answer)
    answer.append(new_point)
    print(f"Добавляем точку: {new_point}")
    print()

for point in answer:
    for i in range(len(old_points)):
        if point[0] == old_points[i][0] and point[1] == old_points[i][1]:
            print(f"A{i+1}({point[0]}, {point[1]})", end="  ")
