# ANSWERS:
# A) 38471 61225
# Б) 142058 25299

from math import dist

fileA = open('27_A_23766.txt')
fileB = open('27_B_23766.txt')
fileA.readline()
fileB.readline()

data = []
for line in fileB:
	x, y = [float(k) for k in line.replace(',', '.').split()]
	data.append([x, y])

print(len(data))

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

def find_centroid_cluster_with_max_points(clusters):
	return centroid(clusters[0]) # тут вручную указываем индекс кластера с максимальной длиной 
	
def find_centroid_cluster_with_min_points(clusters):
	return centroid(clusters[1]) # тут вручную указываем индекс кластера с минимальной длиной

def find_max_distance_between_centroid_and_any_point(clusters):
	cl1 = max([dist(centroid(clusters[0]), point) for point in clusters[0]])
	cl2 = max([dist(centroid(clusters[1]), point) for point in clusters[1]])
	cl3 = max([dist(centroid(clusters[-1]), point) for point in clusters[-1]])
	return max(max(cl1, cl2), cl3)
minn = find_centroid_cluster_with_min_points(clusters)
maxx = find_centroid_cluster_with_max_points(clusters)


Px = int(abs(min([x for x, y in centroids])) * 10000)
Py = int(abs(min([y for x, y in centroids])) * 10000)
Q1 = int(dist(minn, maxx) * 10000)
Q2 = int(find_max_distance_between_centroid_and_any_point(clusters) * 10000)
print(Px, Py, Q1, Q2)