# ANSWERS:
# A) 79724 158994
# Б) 205908 237869

from math import dist

fileA = open('27A_20292.txt')
fileB = open('27B_20292.txt')

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
		neighbours = [p1 for p1 in data if dist(point, p1) < 0.4]
		clusters[-1].extend(neighbours)
		for p1 in neighbours: data.remove(p1)
	print(len(clusters[-1]))

# Среднее расстояние - среднее арифметическое расстояние между всеми парами РАЗЛИЧНЫХ точек в кластере -> сначала нахожим все расстояния, потом определяем среднее арифметическое
def medium_distance(cluster):
	dists = []
	for i in range(len(cluster) -1):
		for j in range(i+1, len(cluster)):
			dists.append(dist(cluster[i], cluster[j]))
	return sum(dists) / len(dists)

distances = [medium_distance(cluster) for cluster in clusters]
Smin = min(distances) * 100000 // 1
Smax = max(distances) * 100000 // 1
print(Smin, Smax)