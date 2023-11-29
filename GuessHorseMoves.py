# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

def gen_move(starting_position):
    if (
        len(starting_position) != 2
        or starting_position[0] not in "ABCDEFGH"
        or starting_position[1] not in "12345678"
    ):
        return "Error position"

    col = ord(starting_position[0]) - ord("A") + 1
    row = int(starting_position[1])

    possible_moves = []

    knight_moves = [
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
    ]

    for move in knight_moves:
        new_col = col + move[0]
        new_row = row + move[1]

        if 1 <= new_col <= 8 and 1 <= new_row <= 8:
            possible_moves.append(chr(new_col + ord("A") - 1) + str(new_row))

    return ", ".join(possible_moves)


print(gen_move("G1"))
