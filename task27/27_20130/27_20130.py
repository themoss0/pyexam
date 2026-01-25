#ANSWERS:
# A) 16730 48696
# Б) 23982 47539

from math import dist

fileA = open('27A_20130.txt')
fileB = open('27B_20130.txt')


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

def diagonal(cluster):
	m = []
	for p1 in cluster:
		for p2 in cluster:
			m.append([dist(p1, p2), p1, p2])
	return max(m)[1:]

diagonals = []
for cl in clusters: diagonals.extend(diagonal(cl))
Px = sum(x for x, y in diagonals) / len(diagonals) * 10000 // 1
Py = sum(y for x, y in diagonals) / len(diagonals) * 10000 // 1
print(Px, Py)


