# Задание 27

## Суть задания:
Даны точки - звезды на небе. Они разбиты на группы точек - кластеры. Предоставленные в задаче файлы - координаты этих звезд. Необходимо разбить их на кластеры и найди их цетроиды(или иное)

## Порядок действий:
- Кластеризация
- Нахождение центроида
- Реализация логики задачи А
- Реализация логики задачи B

## Алгоритм DBScan:
 - Берём случайную точку
 - Для этой точки собираем кластер: 
 - Находим всех соседей на расстоянии х
 - Повторяем такой поиск соседей для всех найденных точек
 - В конечном итоге определим все точки кластера (не останется таких точек, чье расстояние между ней и соседней <= x) 
 
 ## Код(Общий вид):
 `Открытие файлов и базовое присваивание:`
 ```
 # Открытие файла и 'холостой' проход 1 строчки(не нужна!)
fileA = open('27_A_21720.txt')
fileB = open(27_B_21720.txt)
fileA.readline()
fileB.readline()

# Список списков - координаты каждой точки - список
data: list(list) = []

# Присвоение x и y в переменных, используя генератор, разделяющий строку по пробелам 
for line in fileA:
	data_x, data_y = [float(k) for k in line.replace(',','.').split()]
	data.append([data_x, data_y])
print(len(data)) # Выводим общее количество точек
 ```

 `Алгоритм кластеризации:`
 ```
# === АЛГОРИТМ КЛАСТЕРИЗАЦИИ ===
clusters = []
# Пока есть хотя бы одна точка:...
while len(data) != 0:
	# Создаём новый кластер(добавляем список из точек) и выкидываем её из data, чтобы не взять её дважды
	clusters.append([data.pop(0)])
	# Берём все точки последнего кластера
	for point in clusters[-1]:
		# Генерируем список соседей точки из выбранного кластера
		neight = [p1 for p1 in data if dist(point, p1) < 1.4]
		# Расширяем список точек выбранного кластера соседями того же кластера
		clusters[-1].extend(neight)
		# Мы добавили в кластер множество точек, удаляем повторы из основной data
		for p1 in neight: data.remove(p1)
	print(len(clusters[-1]))
# ===============================	
 ```

 `Нахождение цетроида:`
 ```
 # === НАХОЖДЕНИЕ ЦЕНТРОИДА ===
def centroid(cluster):
	# Список, содержащий в будущем внутри себя список - [сумма, точка]
	m = []
	# Находим расстояние между точкой кластера и другой точкой
	# (будет брать сперва саму себя, это нам не помешает)
	for p in cluster:
		sm = sum(dist(p, p1) for p1 in cluster)
		# Добавляем в m список значений - [сумма, точка]. Важно! СПЕРВА СУММА, ПОТОМ ТОЧКА
		m.append([sm, p])
	# Особенность python: min() сработает по левому элементу
	return min(m)[-1] 
# ===============================
 ```

 `Логика для части A`(Нахождение мин. абсциссы/ординаты):
 ```
 centroids = [centroid(cluster) for cluster in clusters]
 Px = int(abs(min([x for x, y in centroids])) * 10000)
 Py = int(abs(min([y for x, y in centroids])) * 10000)
 ```

 `Логика для части Б`(Q1​ - расстояние между центрами кластеров с минимальным и максимальным количеством точек, и Q2​ - максимальное расстояние от центра кластера до точки этого же кластера среди всех кластеров):
 ```
 def find_centroid_cluster_with_max_points(clusters):
	return centroid(clusters[0]) # тут вручную указываем индекс кластера с максимальной длиной 
	
def find_centroid_cluster_with_min_points(clusters): # подразумевается, что дано 3 кластера. Если больше/меньше, дополняем/убираем
	return centroid(clusters[1]) # тут вручную указываем индекс кластера с минимальной длиной

def find_max_distance_between_centroid_and_any_point(clusters):
	cl1 = max([dist(centroid(clusters[0]), point) for point in clusters[0]])
	cl2 = max([dist(centroid(clusters[1]), point) for point in clusters[1]])
	cl3 = max([dist(centroid(clusters[-1]), point) for point in clusters[-1]])
	return max(max(cl1, cl2), cl3)

Q1 = int(dist(minn, maxx) * 10000)
Q2 = int(find_max_distance_between_centroid_and_any_point(clusters) * 10000)
 ```	

 Вывод:
 ```
print(Px, Py, Q1, Q2)
 ```

 ### Аномалии:
 Иногда бывает, что в задачах упоминаются аномалии - точки, которые не относятся ни к одному из кластеров. Чтобы их убрать, после `алгоритма кластеризации` вне цикла требуется написать: 
 ```
 clusters = [cl for cl in clusters if len(cl) > 1]
 ````

 ### Прототипы заданий А и Б: 
 `Расстояние между центрами кластеров:`
 ```
ct0x = [centroids[0][0]]
ct1x = [centroids[1][0]]
ct0y = [centroids[0][1]]
ct1y = [centroids[1][1]]
Px = int(abs(dist(ct0x, ct1x)) * 10000)
Py = int(abs(dist(ct0y, ct1y)) * 10000)
 ```

`Антицентр класстера:` - точка, имеющая максимальную сумму расстояний между остальными точками
 ```
def anti_centroid(cluster):
	m = []
	for point in cluster:
		sm = sum(dist(point, p1) for p1 in cluster)
		m.append([sm, point])
	return max(m)[-1]
 ```

 `Нахождение максимального расстояния между антицентром кластера и точками:`
 ```
def max_dist(cluster, anti_centroid):
	return max(dist(anti_centroid, p1) for p1 in cluster)

md0 = max_dist(clusters[0], anti_centroids[0])
md1 = max_dist(clusters[1], anti_centroids[1])
md2 = max_dist(clusters[2], anti_centroids[2])
Q2 = max(md0, md1, md2) * 10000 // 1
 ```

`Диагональ кластера:`- такой отрезок, что образующие его точки максимально отдалены друг от друга(Максимальное расстояние между двумя точками кластера)
 ```
 Нас интересуют конкретно эти две точки, поэтому берём срез [1:]
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
 ```

 `Среднее расстояние` - среднее арифметическое расстояние между всеми парами РАЗЛИЧНЫХ точек в кластере -> сначала нахожим все расстояния, потом определяем среднее арифметическое
 ```
def medium_distance(cluster):
	dists = []
	for i in range(len(cluster) -1):
		for j in range(i+1, len(cluster)):
			dists.append(dist(cluster[i], cluster[j]))
	return sum(dists) / len(dists)

distances = [medium_distance(cluster) for cluster in clusters]
Smin = min(distances) * 100000 // 1
Smax = max(distances) * 100000 // 1
```