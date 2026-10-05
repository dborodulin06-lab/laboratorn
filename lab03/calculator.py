num1 = float(input())
num2 = float(input())
operation = input().strip()

result = None

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = num1 / num2
else:
    print("Неизвестная операция")

if result is not None:
    print(f"{result:.2f}")
