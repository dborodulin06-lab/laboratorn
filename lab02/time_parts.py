total_seconds = int(input())
total_hours = total_seconds // 3600
ost_seconds = total_seconds % 3600
minut = ost_seconds // 60
seconds = ost_seconds % 60
print(f'{total_hours} ч {minut} мин {seconds} с')