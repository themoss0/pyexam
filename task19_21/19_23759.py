from math import floor

def f(s, m):
    if s <= 30: return m%2==0
    if m == 0: return 0
    h = [
        f(s-3, m-1),
        f(s-5, m-1),
        f(floor(s/4), m-1)
    ]
    return any(h) if m%2 != 0 else all(h)

print(f'19) {min([s for s in range(31, 12100) if f(s, 2)])}') # 124
print(f'20) {[s for s in range(31, 12100) if not f(s, 1) and f(s, 3)][:2]}') # 
print(f'21) {min([s for s in range(31, 12100) if not f(s, 2) and f(s, 4)])}') # 