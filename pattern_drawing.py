# Pattern 1: Right-angled Triangle
n = int(input())
for a in range(n + 1):
    print(a * '*')

# Pattern 2: Square with Hollow Center
m = int(input())
for _ in range(m - (m - 2) - 1):
    print(m * '*')
    for _ in range(m - 2):
        print('*' + (m - 2) * ' ' + '*')
    print(m * '*')

# Pattern 3: Diamond
l = int(input())
for b in range(l):
    print(' ' * (l - b), '*' * (b * 2 + 1))
for b in range(n - 2, -1, -1):
    print(' ' * (l - b), '*' * (b * 2 + 1))

# Pattern 4: Left-angled Triangle
k = int(input())
for c in range(k + 1):
    print((k - c) * '*')

# Pattern 5: Hollow Square
o = int(input())
for _ in range(o - (o - 2) - 1):
    print(o * '*')
    for _ in range(o - 2):
        print('*' + (o - 2) * ' ' + '*')
    print(o * '*')

# Pattern 6: Pyramid
p = int(input())
for d in range(p):
    print(' ' * (p - d), '*' * (d * 2 + 1))
for e in range(p - 2, -1, -1):
    print(' ' * (p - e), '*' * (e * 2 + 1))


