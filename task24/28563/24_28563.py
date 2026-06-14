s = open('task24\\28563\\24_28563.txt').readline()
n = len(s)

max_count_2026 = 0
min_len = n + 1

for l in range(n):
    has_2020 = False
    count_2026 = 0
    
    for r in range(l, n):
        # Проверяем появление 2020 в конце текущей подстроки
        if r - l >= 3 and s[r-3:r+1] == '2020':
            break
        
        # Считаем 2026
        if r - l >= 3 and s[r-3:r+1] == '2026':
            count_2026 += 1
        
        current_len = r - l + 1
        
        if count_2026 > max_count_2026:
            # Новый максимум — обновляем всё
            max_count_2026 = count_2026
            min_len = current_len
        elif count_2026 == max_count_2026 and max_count_2026 > 0:
            # Столько же 2026 — берём минимальную длину
            if current_len < min_len:
                min_len = current_len

print(min_len)