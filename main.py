xA, yA = -1, 22
xB, yB = 17, 1

window_cord = [11, 0, 15, 0]


def find_code(xA, yA, window_cord):
    result = ""
    print(f"Для ({xA}, {yA})")
    if yA > window_cord[0]:
        result += "1"
        print(f"y > {window_cord[0]} - истина")
    else:
        print(f"y < {window_cord[0]} - ложь")
        result += "0"

    if yA < window_cord[1]:
        result += "1"
        print(f"y < {window_cord[1]} - истина")
    else:
        print(f"y > {window_cord[1]} - ложь")
        result += "0"

    if xA > window_cord[2]:
        result += "1"
        print(f"x > {window_cord[2]} - истина")
    else:
        print(f"x < {window_cord[2]} - ложь")
        result += "0"

    if xA < window_cord[3]:
        result += "1"
        print(f"x < {window_cord[3]} - истина")
    else:
        print(f"x > {window_cord[3]} - ложь")
        result += "0"

    print(result)
    return result

def find_intersection(codeA, codeB):
    result = ""
    for i in range(len(codeA)):
        if codeA[i] == codeB[i]:
            result += "0"
        else:
            result += "1"

    print(f"a или b = {result}")

    return result

def find_koef(xA, yA, xB, yB):
    x = xB - xA
    y = yB - yA

    print(f"Перпендикулярный вектор: {-y}, {x}")
    print(f"Уравнение имеет вид: {-y} * (x+{-xB}) + {x} * (y+{-yB}) = 0")

    return [-y, x, -xB, -yB]

def find_points(result, koef, window_cord):
    points = []
    x_koef = koef[0]
    y_koef = koef[1]
    const_koef = koef[0] * koef[2] + koef[1] * koef[3]
    if result[0] == "1":
        print(f"{x_koef} * x + {y_koef} * y + {const_koef} = 0")
        print(f"y = {window_cord[0]}")
        x = round((-const_koef - y_koef * window_cord[0]) / x_koef, 2)
        print(f"x = {x}")
        points.append((x, window_cord[0]))
    if result[1] == "1":
        print(f"{x_koef} * x + {y_koef} * y + {const_koef} = 0")
        print(f"y = {window_cord[1]}")
        x = round((-const_koef - y_koef * window_cord[1]) / x_koef, 2)
        print(f"x = {x}")
        points.append((x, window_cord[1]))
    if result[2] == "1":
        print(f"{x_koef} * x + {y_koef} * y + {const_koef} = 0")
        print(f"x = {window_cord[2]}")
        y = round((-const_koef - x_koef * window_cord[2]) / y_koef, 2)
        print(f"y = {y}")
        points.append((window_cord[2], y))
    if result[3] == "1":
        print(f"{x_koef} * x + {y_koef} * y + {const_koef} = 0")
        print(f"x = {window_cord[3]}")
        y = round((-const_koef - x_koef * window_cord[3]) / y_koef, 2)
        print(f"y = {y}")
        points.append((window_cord[3], y))

    return points

print("Code for A:")
codeA = find_code(xA, yA, window_cord)
print()

print("Code for B:")
codeB = find_code(xB, yB, window_cord)
print()

result = find_intersection(codeA, codeB)
print()

point_codes = [codeA, codeB]

koef = find_koef(xA, yA, xB, yB)
print()

points = find_points(result, koef, window_cord)

points.append((xA, yA))
points.append((xB, yB))

print(points)

points_codes = []

for i in range(len(points)):
    print()
    points_codes.append(find_code(points[i][0], points[i][1], window_cord))

print(points_codes)

answer = []
for i in range(len(points_codes)):
    if points_codes[i] == "0000":
        answer.append(points[i])

print(answer)