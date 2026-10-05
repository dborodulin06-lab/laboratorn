a = int(input())
if 0 <= a <= 24:
    print('начало')
elif 25 <= a <= 84:
    print('В процессе')
elif 85 <= a <= 100:
    print('Завершение')
else:
    print('Ошибка диапазона')