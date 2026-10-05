num = 0
cnt = 0
while num <= 0:
    num = int(input())
    if num <= 0:
        cnt += 1
n2 = num ** 2
print(f'{n2}, попыток - {cnt}')