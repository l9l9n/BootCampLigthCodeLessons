k = int(input('Обхват по бюсту: '))
m = int(input('Обхват по бедру: '))
n = int(input('Обхват по талии: '))
t = int(input('Рост: '))
p = int(input('Вес: '))

l = (k * m * t) / ((n**2) * p)
print(round(l))