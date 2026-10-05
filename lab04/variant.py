n = int(input())
cnt = 0
numbers = []
if n >= 0:
    for i in range(n):
        num = int(input())
        if num < 0 and num % 2 != 0:
            numbers.append(num)
            cnt += 1
        else:
            numbers = []
            cnt = 0

print(f'сумма {sum(numbers)}')
print(f'количество {cnt}')