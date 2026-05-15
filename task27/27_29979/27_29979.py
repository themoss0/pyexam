from math import dist

fileA = open('task27\\27_29979\\27_A_29979.txt')
fileB = open('task27\\27_29979\\27_B_29979.txt')

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

def find_x(cl, ctr):
    c = 0
    for point in cl:
        if point[0] <= ctr[0]:
            c += 1
    return c

def dist_ctr(ctr1, ctr2):
    return dist(ctr1, ctr2)

def find_dots(cl, ctr):
    c = 0
    for point in cl:
        if ctr[0] - 1 <= point[0] <= ctr[0]+1 and ctr[1] - 1 <= point[1] <= ctr[1] + 1:
            c += 1
    return c

A1 = find_x(clusters[0], centroids[0])
A2 = dist_ctr(centroids[0], centroids[1]) * 10_000 // 1
B1 = find_dots(clusters[1], centroids[1])
B2 = abs(centroids[0][1] - centroids[2][1]) * 10_000 // 1
print(A1, A2)
print(B1, B2)
