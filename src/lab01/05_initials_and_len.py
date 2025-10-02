
name = input('Ф.И.О: ').strip().upper()

parts = name.split()

normalized_name = " ".join(parts)

print('Iniciais: ', end='')
for part in parts:
    print(part[0], end=' ')

symbols_count = len(normalized_name)
print(f'\nQuantidade: {symbols_count}')
