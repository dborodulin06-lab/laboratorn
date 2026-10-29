text = input()
numbers = list(map(int, text.split()))
result = [x for x in numbers if x > 0]
sorted_result = sorted(result)
print("Список:", result)
print("Количество:", len(result))
print("Сумма:", sum(result))
print("Отсортированная копия:", sorted_result)