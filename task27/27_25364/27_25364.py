# ANSWERS:
# A) 58605 128643
# Б) 

from math import dist

fileA = open('27_A_25364.txt')
fileB = open('27_B_25364.txt')

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

def centroid(cluster):
	m = []
	for point in cluster:
		sm = sum(dist(point, p1) for p1 in cluster)
		m.append([sm, point])
	return min(m)[-1]

centroids = [centroid(cluster) for cluster in clusters]
d = [1.0, 1.0]
P1 = min(dist(d, centre) for centre in centroids) * 10000 // 1
P2 = max(dist(d, centre) for centre in centroids) * 10000 // 1
Q1 = len([p1 for p1 in clusters[0] if dist(centroids[0], p1) <= 1.2])
Q2 = len([p1 for p1 in clusters[0] if dist(centroids[0], p1) <= 0.75])
print(P1, P2, Q1, Q2) 

