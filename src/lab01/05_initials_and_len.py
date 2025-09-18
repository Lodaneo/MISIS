name = str(input('Ф.И.О:')).strip().upper()
div = name.split()
print(f'Инициалы: ',end = '')
for c in range(len(div)):
    sep = (div[c])
    print(f'{sep[0]}',end = ' ') 
print(f'\nДлина(Символов):{len(name)}')
