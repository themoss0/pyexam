#ANSWERS: 
# A) 15342 115607
# Б) ? ?

from math import dist

fileA = open('27A_25448.txt')
fileB = open('27B_25448.txt')
fileA.readline()
fileB.readline()

data = []

for line in fileB:
	x, y = [float(k) for k in line.replace(',', '.').split()]
	data.append([x, y])
print(len(data))

clusters = []
while len(data) != 0:
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

def q1():
	m = []
	for point in clusters[1]:
		sm = sum(dist(point, p1) for p1 in clusters[1] if point != p1)
		m.append([sm, point])
	return sum(m[i][0] for i in range(len(m)-1))

ct0x = [centroids[0][0]]
ct1x = [centroids[1][0]]
ct0y = [centroids[0][1]]
ct1y = [centroids[1][1]]
Px = int(abs(dist(ct0x, ct1x)) * 10000)
Py = int(abs(dist(ct0y, ct1y)) * 10000)

print(Px, Py, q1())
