total = int(input())
capacity = int(input())
filled_units = total // capacity
remainder = total % capacity
min_units = (total + capacity - 1) // capacity

print(filled_units)
print(remainder)
print(min_units)