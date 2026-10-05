n = int(input())
first_num = int(input())
current_sum = first_num
positive_count = 1 if first_num > 0 else 0
maximum = first_num


for _ in range(n - 1):
    num = int(input())
    current_sum += num
    if num > 0:
        positive_count += 1
    if num > maximum:
        maximum = num

print(current_sum)
print(positive_count)
print(maximum)