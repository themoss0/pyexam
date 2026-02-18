# ANSWERS:
# A) 115252 58612
# Б) 9202 8993


from math import dist

fileA = open('27A_25447.txt')
fileB = open('27B_25447.txt')

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
clusters = [c for c in clusters if len(c) > 1]

def centroid(cluster):
    m = []
    for point in cluster:
        sm = sum(dist(point, p1) for p1 in cluster)
        m.append([sm, point])
    return min(m)[-1]

def medium_dist_between_centroids(cluster, centr):
    c = centr
    sm = sum(dist(c, p1) for p1 in cluster if p1 != c)
    return sm / (len(cluster)-1)
        

centroids = [centroid(cluster) for cluster in clusters]


Px = abs(min(x for x, y in centroids)) * 10000 // 1
Py = abs(min(y for x, y in centroids)) * 10000 // 1
Q1 = abs(medium_dist_between_centroids(clusters[2], centroids[2])) * 10000 // 1
Q2 = abs(medium_dist_between_centroids(clusters[0], centroids[0])) * 10000 // 1

print(Px, Py, Q1, Q2)
