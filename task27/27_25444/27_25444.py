# ANSWERS:
# A) 59674 83769
# Б) 5651 9761

from math import dist

fileA = open('27A_25444.txt')
fileB = open('27B_25444.txt')

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
		neighbours = [p1 for p1 in data if dist(point, p1) < 0.28]  # для файла A надо < 1
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

# Файл А:

# Образуем массив расстояний от центроида одного кластера до всех точек другого, возвращаем список
def distance_between_centroid_and_any_point(other_cluster, centroid):
	return [dist(centroid, p1) for p1 in other_cluster]

# Отбираем значения min и max, используя различные кластеры и центроиды 
cl0cr1_min = min(distance_between_centroid_and_any_point(clusters[0], centroids[1]))
cl1cr0_min = min(distance_between_centroid_and_any_point(clusters[1], centroids[0]))
cl0cr1_max = max(distance_between_centroid_and_any_point(clusters[0], centroids[1]))
cl1cr0_max = max(distance_between_centroid_and_any_point(clusters[1], centroids[0]))

# Файл Б:

def max_distance_between_centroids():
	return max(dist(centroids[i], centroids[j]) for i in range(len(centroids)-1) for j in range(i+1, len(centroids)))

def min_distance_between_centroids():
	return min(dist(centroids[i], centroids[j]) for i in range(len(centroids)-1) for j in range(i+1, len(centroids)))
Px = abs(min(cl0cr1_min, cl1cr0_min)) * 10000 // 1
Py = abs(max(cl0cr1_max, cl1cr0_max)) * 10000 // 1
Q1 = abs(min_distance_between_centroids()) * 10000 // 1
Q2 = abs(max_distance_between_centroids()) * 10000 // 1
print(Px, Py, Q1, Q2)