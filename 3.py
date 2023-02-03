q = int(input('Первое число'))
w = int(input('Второе число'))
e = int(input('Третье число'))
if q < w and q < e:
    r = q
elif w < q and w < e:
    r = w
elif e < q and e < w:
    r = e
print('  ')
print('Наименьшое число среди всех', r)