from math import dist

fileA = open('27A_25446.txt')
fileB = open('27B_25446.txt')

fileA.readline()
fileB.readline()

data = []

for line in fileB:
	x, y = [float(k) for k in line.replace(',', '.').split()]
	data.append([x, y])

clusters = []
while len(data) != 0:
	clusters.append([data.pop(0)])
	for point in clusters[-1]:
		neighbours = [p1 for p1 in data if dist(point, p1) < 2]
		clusters[-1].extend(neighbours)
		for p1 in neighbours: data.remove(p1) 
	print(len(clusters[-1]))
clusters = [cl for cl in clusters if len(cl) > 1]

def centroid(cluster):
	m = []
	for point in cluster:
		sm = sum(dist(point, p1) for p1 in cluster)
		m.append([sm, point])
	return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]


def find_centroid_cluster_with_max_points(clusters):
	return centroid(clusters[0])
	
def find_centroid_cluster_with_min_points(clusters):
	return centroid(clusters[1])

minn = find_centroid_cluster_with_min_points(clusters)
maxx = find_centroid_cluster_with_max_points(clusters)

Px = int(max([x for x, y in centroids]) * 10000)
Py = int(max([y for x, y in centroids]) * 10000)
Q1 = int(abs(dist(minn, maxx)) * 10000)
print('=============')
print(minn, maxx)

print(Px, Py, Q1) # 66679 127423
