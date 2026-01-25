# ANSWERS:
# A) 107002 323741
# Б) 58778 151839

from math import dist

fileA = open('27_A_23284.txt')
fileB = open('27_B_23284.txt')
fileA.readline()
fileB.readline()

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
clusters = [cl for cl in clusters if len(cl) > 1]
def centroid(cluster):
	m = []
	for point in cluster:
		sm = sum(dist(point, p1) for p1 in cluster)
		m.append([sm, point])
	return min(m)[-1]

centroids = [centroid(cluster) for cluster in clusters]

def max_distance_between_centroids():
	return max(dist(centroids[i], centroids[j]) for i in range(len(centroids)-1) for j in range(i+1, len(centroids)))

def min_distance_between_centroids():
	return min(dist(centroids[i], centroids[j]) for i in range(len(centroids)-1) for j in range(i+1, len(centroids)))
Px = sum(x for x, y in centroids) * 10000 // 1
Py = sum(y for x, y in centroids) * 10000 // 1
Q1 = abs(min_distance_between_centroids()) * 10000 // 1
Q2 = abs(max_distance_between_centroids()) * 10000 // 1
print(Px, Py, Q1, Q2)