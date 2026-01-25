# ANSWERS:
# A) 18236 93042
# Б) 9163 1646

from math import dist

fileA = open('27A_25441.txt')
fileB = open('27B_25441.txt')
fileA.readline()
fileB.readline()

data = []
for line in fileB:
	x, y = [float(k) for k in line.replace(',','.').split()]
	data.append([x, y])
print(len(data))
print('----')

clusters = []
while data:
	clusters.append([data.pop(0)])
	for point in clusters[-1]:
		neighbours = [p1 for p1 in data if dist(point, p1) < 0.2]
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

def q2(clusters):
	cl1 = max([dist(centroid(clusters[0]), point) for point in clusters[0]])
	cl2 = max([dist(centroid(clusters[1]), point) for point in clusters[1]])
	cl3 = max([dist(centroid(clusters[-1]), point) for point in clusters[-1]])
	return int(abs(max(max(cl1, cl2), cl3))* 10000)

centroids = [centroid(cluster) for cluster in clusters]

ct0x = [centroids[0][0]]
ct1x = [centroids[1][0]]
ct0y = [centroids[0][1]]
ct1y = [centroids[1][1]]

Px = int(abs(dist(ct0x, ct1x)) * 10000)
Py = int(abs(dist(ct0y, ct1y)) * 10000)

maxx = centroid(clusters[0])
minn = centroid(clusters[1])

Q1 = int(abs(dist(minn, maxx)) * 10000)

print(Px, Py, Q1, q2(clusters))