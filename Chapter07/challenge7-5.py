a = [8, 19, 148, 4]
b = [9, 1, 33, 83]
c = a[0]*b[0]
d = a[1]*b[1]
e = a[2]*b[2]
f = a[3]*b[3]
g = [c,d,e,f]
print(g)
print("上は間違い")
lista =[8, 19, 148, 4]
listb =[9, 1, 33, 83]
result = []
for h in lista:
    for i in listb:
        result.append(h * i)
print(result)
