#задача1
a = str(input("Введите строку:"))
a = a.upper()
n1 = a.count('G')
n2 = a.count('C')
x = len (a)
# сумма знаков g and c
n = n1+n2
# процент символов g and c в строке
r = (n/x)*100
p = round(r, 1)
print (p)
#################
a = input()
res1 = a.upper()
k = res1.count('C')
k2 = res1.count('G')
k3 = int(k) + int(k2)
k4 = res1.count('')
result = (k3 / (k4 - 1)) * 100
print(result)
#################



