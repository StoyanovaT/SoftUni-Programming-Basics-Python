figure = str(input())
if figure == "square":
    side = float(input())
    S = side * side
    print(f"{S:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    S = side_a * side_b
    print(f"{S:.3f}")
elif figure == "circle":
    radius = float(input())
    import math
    S = math.pi * radius * radius
    print(f"{S:.3f}")
elif figure == "triangle":
    side = float(input())
    height = float(input())
    S = (side * height) / 2
    print(f"{S:.3f}")
