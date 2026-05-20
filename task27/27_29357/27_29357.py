from math import dist

# 44694 69754
# 138716 34029

fileA = open('task27\\27_29357\\27_A_29357.txt')
fileB = open('task27\\27_29357\\27_B_29357.txt')

data = []
for line in fileA:
    x_pos, y_pos, info = line.replace(',','.').split()
    x_pos = float(x_pos)
    y_pos = float(y_pos)
    # Сказано, что для белого карлика не даны числа, поэтому, чтобы
    # при переборах не было ошибки с выходами за границы строки, мы добавим
    # просто 2 пробела в начало и сохраним:
    if info == 'VII': info = "  VII" 
    data.append([x_pos, y_pos, info])
print("DEBUG LOG\n=============")
print(f'Кол-во точек в файле: {len(data)}')
print(f'Пример элемента в data: {data[0]}\n{type(data)=}\n{type(data[0])=}')
print('=============')
print()

clusters = []
n = 1
while data:
    clusters.append([data.pop(0)])
    for point in clusters[-1]:
        neighbors = [p1 for p1 in data if dist(point[:2], p1[:2]) < 1]
        clusters[-1].extend(neighbors)
        for p1 in neighbors: data.remove(p1)
    print(f'{n}) {len(clusters[-1])}')
    n += 1

def centroid(cluster):
    m = []
    for point in cluster:
        sm = sum(dist(point[:2], p1[:2]) for p1 in cluster)
        m.append([sm, point])
    return min(m)[-1]

centroids = [centroid(cl) for cl in clusters]

#абсцисса и ордината красного гиганта, ближайшего к центру кластера, 
# который содержит наименьшее количество точек. 
# для файла А - это 1 кластер(114 точка), поэтому это clusters[0]


# Находим ближайшего красного гиганта к центроиду кластера
def find_red_giant_A(ctr, cl):
    m = []
    for point in cl:
        # point[2] - это та самая информация, 
        # которую мы храним(F6II, к примеру)
        if point[2][0] == 'M' and point[2][2:] == "III":
            d = dist(ctr[:2], point[:2])
            m.append([d, point])
    return min(m)[-1]

Ax = abs(find_red_giant_A(centroids[0], clusters[0])[0]) * 10_000 // 1
Ay = abs(find_red_giant_A(centroids[0], clusters[0])[1]) * 10_000 // 1


# Считаем число оранжевых гигантов в кластере 
def find_orange_giant(cl):
    count = 0
    for point in cl:
        if point[2][0] == "K" and point[2][2:] == "III":
            count += 1
    return count


# Находим максимальное расстояние между желтыми карликами кластера
def find_max_dist(cl):
    m = []
    for point in cl:
        for p1 in cl:
            if (point[2][0] == 'G' and point[2][2:] == "V") and (p1[2][0] == 'G' and p1[2][2:] == 'V'):
                d = dist(point[:2], p1[:2])
                m.append(d)
    return max(m)

# og1 = find_orange_giant(clusters[0])
# og2 = find_orange_giant(clusters[1])
# og3 = find_orange_giant(clusters[2])

# md1 = find_max_dist(clusters[0])
# md2 = find_max_dist(clusters[1])
# md3 = find_max_dist(clusters[2])

# B1 = dist(centroids[2][:2], centroids[0][:2]) * 10_000 // 1
# B2 = max(md1, md2, md3) * 10_000 // 1

print(Ax, Ay)
# print(B1, B2)

# print()
# print("DEBUG LOG\n=============")
# print(f"Данные о оранжевых гигантах кластеров:\n{og1=}\n{og2=}\n{og3=}")
# print("=============")