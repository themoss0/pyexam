#ANSWERS:
# A) 27708 189345
# Б) 187711 49105
from math import dist

fileA = open('27A_24985.txt')
fileB = open('27B_24985.txt')
fileA.readline()
fileB.readline()

data = []

for line in fileB:
	x, y = [float(k) for k in line.replace(',','.').split()]
	data.append([x, y])
print(len(data))
print()


clusters = []
while len(data) != 0:
	clusters.append([data.pop(0)])
	for point in clusters[-1]:
		neighbours = [p1 for p1 in data if dist(point, p1) < 1]
		clusters[-1].extend(neighbours)
		for p1 in neighbours: data.remove(p1)
	print(len(clusters[-1])) 
clusters = [cl for cl in clusters if len(cl) > 1]
# Антицентр класстера - точка, имеющая максимальную сумму расстояний между точками
def anti_centroid(cluster):
	m = []
	for point in cluster:
		sm = sum(dist(point, p1) for p1 in cluster)
		m.append([sm, point])
	return max(m)[-1]

# Нахождение максимального расстояния между антицентром кластера и точками
def max_dist(cluster, anti_centroid):
	return max(dist(anti_centroid, p1) for p1 in cluster)

anti_centroids = [anti_centroid(cluster) for cluster in clusters]
Px = abs(max(x for x, y in anti_centroids) * 10000) // 1
Py = abs(max(y for x, y in anti_centroids) * 10000) // 1
md0 = max_dist(clusters[0], anti_centroids[0])
md1 = max_dist(clusters[1], anti_centroids[1])
md2 = max_dist(clusters[2], anti_centroids[2])
Q1 = dist(anti_centroids[0], anti_centroids[1]) * 10000 // 1
Q2 = max(md0, md1, md2) * 10000 // 1
print(Px, Py, Q1, Q2)