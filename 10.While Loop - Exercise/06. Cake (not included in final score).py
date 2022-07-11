height = int(input())
width = int(input())
cake_pieces = height * width


while True:
    command = input()
    if cake_pieces > 0:
        if command == "STOP":
            print(f"{cake_pieces} pieces are left." )
            break

        pieces_taken = int(command)
        if cake_pieces <= pieces_taken:
            cake_pieces = abs(cake_pieces - pieces_taken)
            print(f"No more cake left! You need {cake_pieces} pieces more.")
            break
        else:
            cake_pieces -= pieces_taken

# Решение на лектора:
# width = int(input())
# length = int(input())
# cake_size = width * length
#
# while cake_size > 0:
#     current_pieces_from_cake = input()
#
#     if current_pieces_from_cake == "STOP":
#         break
#
#     cake_size -= int(current_pieces_from_cake)
#
# if cake_size > 0:
#     print(f"{cake_size} pieces are left." )
# else:
#     print(f"No more cake left! You need {abs(cake_size)} pieces more.")