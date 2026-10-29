text = input()
numbers = list(map(int, text.split()))
new_numbers = [abs(number) for number in numbers]
print("Исходный список:", numbers)
print("Новый список:", new_numbers)
