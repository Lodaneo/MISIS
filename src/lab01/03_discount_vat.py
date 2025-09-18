price = float(input('введите цену: '))
discount = float(input('введите скидку: '))
vat = float(input('введите налог: '))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f}₽')
print(f'НДС: {vat_amount:.2f}₽')
print(f'Итого к оплате: {total:.2f}₽')