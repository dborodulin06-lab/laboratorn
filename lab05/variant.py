text = input()
words = text.split()
count = 0

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if cleaned:
        print(cleaned)
        count += 1
if count == 0:
    print("Нет совпадений")

print("Количество:", count)