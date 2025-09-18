m = int(input('Минуты: '))
min = m
s = 0
while (min >= 60) :
    min = min - 60
    s = s + 1
c = m - (s * 60)
print(f'{s} : {c}')