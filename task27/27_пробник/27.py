from math import dist

fileA = open('27A.txt')
fileB = open('27B.txt')

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
	x, y = 0, 0
	for _x, _y in cluster:
		x += _x
		y += _y
	avg_x = x / len(cluster)
	avg_y = y / len(cluster)
	return [avg_x, avg_y] 

centroids = [centroid(cluster) for cluster in clusters]

Px = sum([x for x, y in centroids]) / len(centroids) * 10000 // 1
Py = sum([y for x, y in centroids]) / len(centroids) * 10000 // 1

print(Px, Py)
# A) 20490 31182
