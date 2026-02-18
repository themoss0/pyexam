# Task 23452

def f(s, m):
    if (s >= 231): return m%2==0
    if (m == 0): return 0
    h = [
        f(s+3, m-1),
        f(s*3, m-1)
    ]
    return any(h) if m%2!=0 else all(h)

s = [x for x in range(10, 121)]
print(min(x for x in s if f(x, 2)))
print([x for x in s if not f(x, 1) and f(x, 3)][:2])
print(min(x for x in s if not f(x, 2) and f(x, 4)))