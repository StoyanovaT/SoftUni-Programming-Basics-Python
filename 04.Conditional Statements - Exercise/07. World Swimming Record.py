from math import floor

record = float(input())
distance_meters = float(input())
time_seconds_1meter = float(input())

extra_time_slowing = floor(distance_meters / 15) * 12.5

ivan_time = distance_meters * time_seconds_1meter + extra_time_slowing

if ivan_time < record:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    seconds_slower = ivan_time - record
    print(f"No, he failed! He was {seconds_slower:.2f} seconds slower.")