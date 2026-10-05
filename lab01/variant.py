zakaz = input('заказ: ')
name_zak = input('имя заказчика: ')

# позиция 1
name1 = input('название позиции: ')
quantity1 = int(input('колличество: '))
price1 = float(input('цена: '))

# позиция 2
name2 = input('название позиции: ')
quantity2 = int(input('колличество: '))
price2 = float(input('цена: '))

# доставка и сумма
dost = float(input('стоимость доставки: '))
summ = float(input('внесенная сумма: '))

# расчеты
cost_pos1 = quantity1 * price1
cost_pos2 = quantity2 * price2
total_cost = cost_pos1 + cost_pos2
total_with_delivery = total_cost + dost
total_units = quantity1 + quantity2
change = summ - total_with_delivery

print("\n" + "="*40)
print(f"Заказ: {zakaz}")
print(f"Заказчик: {name_zak}")
print("-"*40)
print(f"{'Название':<20} | {'Количество':<12} | {'Цена':<10} | {'Стоимость':<10}")
print("-"*40)
print(f"{name1:<20} | {quantity1:<12} | {price1:<10.2f} | {cost_pos1:<10.2f}")
print(f"{name2:<20} | {quantity2:<12} | {price2:<10.2f} | {cost_pos2:<10.2f}")
print("-"*40)
print(f"Стоимость товаров без доставки: {total_cost:<10.2f}")
print(f"Общая сумма с доставкой: {total_with_delivery:<10.2f}")
print(f"Общее количество единиц: {total_units:<10}")

print(f"Сдача: {change:<10.2f}")
print("="*40)
print("\n" + "Денежные значения с двумя знаками после точки:")
print(f"Стоимость товаров без доставки: {total_cost:<10.2f}")
print(f"Общая сумма с доставкой: {total_with_delivery:<10.2f}")
print(f"Общее количество единиц: {total_units}")
print(f"Сдача: {change:<10.2f}")
