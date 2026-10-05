price = int(input())
count = int(input())
paid = int(input())
if paid >= price * count:
    print(f'стоимость {price * count}, сдача {paid - (price * count)}')
else:
    print('Не правильные данные')