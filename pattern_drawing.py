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

# Pattern 7: Square Frame
o = int(input())
for _ in range(o - (o - 2) - 1):
    print(o * '*')
    for _ in range(o - 2):
        print('*' + (o - 2) * ' ' + '*')
    print(o * '*')

# Pattern 8: Number pyramid
n = int(input())
for a in range(n):
    for b in range(n):
        if b % 2 == 0:
            if (b >= (abs(4 - a) * 2 - 1)):
                print(b + 2, end='')
            else:
                print(' ', end='')
        else:
            print(' ', end='')
    print()

def triangle(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

    for j in range(1, n + 1):
        print(j, end=' ')
    print()

    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
    return ''

print(triangle(int(input())))
