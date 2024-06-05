xA, yA = 8.43, 11

xB, yB = 15, 3.33

print(f"A({xA}, {yA}), B({xB}, {yB})")

def modal(num):
    if num > 0:
        return num
    elif num < 0:
        return -num
    else:
        return num

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

L = max(modal(round(xB) - round(xA)), modal(round(yB) - round(yA)))
print(f"L = max(xB - xA, yB - yA) + 1 = max({round(xB) - round(xA), round(yB) - round(yA)} = {L}")

points = [(xA, yA)]

koef1 = round((xB - xA) / L, 3)
koef2 = round((yB - yA) / L, 3)

print(f"(xB - xA)/L = ({xB} - {xA}) / {L} = {koef1}")
print(f"(yB - yA)/L = ({yB} - {yA}) / {L} = {koef2}")

x = xA
y = yA
for i in range(L - 1):
    print(f"Итерация {i + 1}")
    print(f"x = {x} + {koef1}", end = "")
    x = round(x + koef1, 3)
    print(f" = {x}")
    print(f"y = {y} + {koef2}", end = "")
    y = round(y + koef2, 3)
    print(f" = {y}")
    points.append((round(x), round(y)))
    print()

points.append((round(xB), round(yB)))
print(points)