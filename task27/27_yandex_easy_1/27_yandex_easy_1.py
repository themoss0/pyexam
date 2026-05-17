from math import dist

# 92256 258611
# 33863 170816
fileA = open('task27\\27_yandex_easy_1\\27_А.txt')
fileB = open('task27\\27_yandex_easy_1\\27_Б.txt')
fileA.readline()
fileB.readline()

data = []
for line in fileB:
    x, y = [float(k) for k in line.replace(',', '.').split()]
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

def centroid(cl):
    m = []
    for point in cl:
        sm = sum(dist(point, p1) for p1 in cl)
        m.append([sm, point])
    return min(m)[-1]

centroids = [centroid(cl) for cl in clusters if len(cl) > 1]

def min_dist(cl1, cl2):
  m = []
  for p in cl1:
    for p1 in cl2:
      m.append(dist(p, p1))
  return min(m)

def max_dist(cl1, cl2):
  m = []
  for p in cl1:
    for p1 in cl2:
      m.append(dist(p, p1))
  return max(m)

mc0 = min_dist(clusters[0], clusters[1])
mc1 = min_dist(clusters[1], clusters[2])
mc2 = min_dist(clusters[0], clusters[2])

mmc0 = max_dist(clusters[0], clusters[1])
mmc1 = max_dist(clusters[1], clusters[2])
mmc2 = max_dist(clusters[0], clusters[2])

Px = abs(sum(x for x, y in centroids)) * 10_000 // 1
Py = abs(sum(y for x, y in centroids)) * 10_000 // 1
Q1 = min(mc0, min(mc1, mc2)) * 10_000 // 1
Q2 = max(mmc0, max(mmc1, mmc2)) * 10_000 // 1

print(Px, Py)
print(Q1, Q2)