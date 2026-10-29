text = input()
numbers = list(map(int, text.split()))

if not numbers:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for i, number in enumerate(numbers):
        if number == maximum:
            positions.append(i)

    print(positions)