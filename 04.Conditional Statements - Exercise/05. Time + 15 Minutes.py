hour = int(input())
minute = int(input())
total_time_in_minutes = hour * 60 + minute + 15
current_hour = total_time_in_minutes // 60
current_minutes = total_time_in_minutes % 60
if current_hour > 23:
    print(f"0:{current_minutes:02d}")
else:
    print(f"{current_hour}:{current_minutes:02d}")