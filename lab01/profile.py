family = input('ввод')
name = input('ввод')
grupp = input('ввод')
town = input('ввод')
age = int(input('ввод'))
b_pred = input('ввод')
hours_week = float(input('ввод'))
if 1 <= age >= 120 and hours_week > 0:
    print('полное имя: ', name, family)
    print('возраст через 4 года: ', age + 4)
    print(f'время подготовки за 4 недели: {hours_week * 4:.2f}')
    print(f'среднее время подготовки в день: {(hours_week / 7):.2f} часов')
else:
    print('неправильный ввод данных')