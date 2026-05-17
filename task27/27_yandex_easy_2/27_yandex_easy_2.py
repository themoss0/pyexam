from math import dist

# 69663 192156
# 867 161306

fileA = open('task27\\27_yandex_easy_2\\27_A.txt')
fileB = open('task27\\27_yandex_easy_2\\27_Б(1).txt')
fileA.readline()
fileB.readline()



data = []
for line in fileB:
    x, y = [float(k) for k in line.replace(',', '.').split()]
    data.append([x, y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for point in clusters[-1]:
        neighbours = [p1 for p1 in data if dist(point, p1) < 1]
        clusters[-1].extend(neighbours)
        for p1 in neighbours: data.remove(p1)
    print(len(clusters[-1]))

clusters = [cl for cl in clusters if len(cl) > 1]

def centroid(cl):
    m = []
    for point in cl:
        sm = sum(dist(point, p1) for p1 in cl)
        m.append([sm, point])
    return min(m)[-1]

centroids = [centroid(cl) for cl in clusters]

Px = abs(max(centroids[0][0], centroids[1][0])) * 10_000 // 1
Py = abs(max(centroids[0][1], centroids[1][1])) * 10_000 // 1

Q1 = abs(centroids[2][0] - centroids[0][0]) * 10_000 // 1
Q2 = abs(centroids[2][1] - centroids[0][1]) * 10_000 // 1

print(Px, Py)
print(Q1, Q2)