# 346070 215898
# 455364 406022

from math import dist

fileA = open('task27\\27_18678_hard\\27A_18678.txt')
fileB = open('task27\\27_18678_hard\\27B_18678.txt')

data = []
for line in fileB:
    x, y = [float(k) for k in line.replace(',','.').split()]
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

def centroid(cl):
    m = []
    for point in cl:
        sm = sum(dist(point, p1) for p1 in cl)
        m.append([sm, point])
    return min(m)[-1]

centroids = [centroid(cl) for cl in clusters]

def Px(ctr1, ctr2, ctr3):
    return (ctr1[0] + ctr2[0] + ctr3[0]) / 3

def Py(ctr1, ctr2, ctr3):
    return (ctr1[1] + ctr2[1] + ctr3[1]) / 3

px = Px(centroids[0], centroids[1], centroids[2]) * 100_000 // 1
py = Py(centroids[0], centroids[1], centroids[2]) * 100_000 // 1
print(px, py)
