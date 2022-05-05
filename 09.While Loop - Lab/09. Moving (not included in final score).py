width = int(input())
length = int(input())
height = int(input())

v_apartment = width * length * height
all_boxes = 0
ap_space_left = 0
command = input()

while command != "Done":
    boxes = int(command)
    all_boxes += boxes
    ap_space_left = v_apartment - all_boxes
    if ap_space_left <= 0:
        print(f"No more free space! You need {abs(ap_space_left)} Cubic meters more.")
        break
    command = input()
else:
    print(f"{ap_space_left} Cubic meters left.")



