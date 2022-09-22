n = int(input())

x = (n // 10) % 10 * 10
y = (n // 1000) % 10 * 1000

print(n + x + y)