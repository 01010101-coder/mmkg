points = [(8, -8), (10, 0), (7, 3), (-5, 10), (-5, 1),
          (-4, 0), (-7, -1), (-3, -5), (-4, -2)]

def oktan_ugol(point):
    x = point[0]
    y = point[1]

    if 0 <= y < x:
        return 1
    elif 0 < x <= y:
        return 2
    elif 0 <= -x < y:
        return 3
    elif 0 < y <= -x:
        return 4
    elif x < y <= 0:
        return 5
    elif y <= x < 0:
        return 6
    elif y < -x <= 0:
        return 7
    else:
        return 8

def vector(point1, point2):
    return (point2[0] - point1[0], point2[1] - point1[1])

def opredelitel(point1, point2):
    opredelitel = (point1[0] * point2[1]) - (point1[1] * point2[0])
    if opredelitel > 0:
        result = 1
    elif opredelitel < 0:
        result = -1
    else:
        result = 0

    return result

vectors = []

for i in range(len(points) - 1):
    vectors.append(vector(points[i], points[(i + 1)]))

vectors.append(vector(points[-1], points[0]))

oktan_ugols = []
for vector in vectors:
    oktan_ugols.append(oktan_ugol(vector))

print(oktan_ugols)

oktan_ugol_difs = []
for i in range(len(oktan_ugols) - 1):
    oktan_ugol_difs.append(oktan_ugols[i+1] - oktan_ugols[i])

oktan_ugol_difs.append(oktan_ugols[0] - oktan_ugols[-1])

print(oktan_ugol_difs)

for i in range(len(oktan_ugol_difs)):
    while(abs(oktan_ugol_difs[i]) > 4 or oktan_ugol_difs[i] == 0):
        oktan_ugol_difs[i] += opredelitel(points[i-1], points[i])

print(oktan_ugol_difs)
