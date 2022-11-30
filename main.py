a = int(input("Длина: "))
b = int(input("Ширина: "))
s = a * b;
print("Площадь прямоугольника: ", s)

a = int(input("Длина: "))
b = int(input("Ширина: "))
p = (a + b) * 2;
print("Периметр прямоугольника: ", p)





n = int(input())
for i in range(n):
    k1 = n - i - 1
    k2 = n + i - 1
    for j in range(k2 + 1):
        print('*' if j >= k1 else ' ', end='')
    print()
    