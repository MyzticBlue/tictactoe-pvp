cells = ' ' * 9
matrix = [[a for a in cells[i:i + 3]] for i in range(0, len(cells), 3)]


def input_element(m, string1):
    user_input = input("Enter the coordinates:")

    if user_input.isalpha():
        print("You should enter numbers!")
        return m, 1
    x, y = user_input.split()
    if x.isalpha() or y.isalpha():
        print("You should enter numbers!")
        return m, 1
    x = int(x)
    y = int(y)
    if x > 3 or y > 3 or x < 1 or y < 1:
        print("Coordinates should be from 1 to 3!")
        return m, 1
    elif m[3 - y][x - 1] != '_' and m[3 - y][x - 1] != ' ':
        print("This cell is occupied! Choose another one!")
        return m, 1
    else:
        m[3 - y][x - 1] = string1
        print('-' * 9)
        for i in range(3):
            print(f"| {m[i][0]} {m[i][1]} {m[i][2]} |")
        print('-' * 9)
        return m, 0


def print_screen(m):
    print('-' * 9)
    for i in range(3):
        print(f"| {m[i][0]} {m[i][1]} {m[i][2]} |")
    print('-' * 9)


def no_of_element(m, letter):
    count = 0
    for i in range(3):
        for j in range(3):
            if m[i][j] == letter:
                count += 1
    return count


def check_winner(m):
    wins = 0
    winner = ''
    # row check
    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2]:
            winner = m[i][0]
            wins += 1

    # column check
    for j in range(3):
        if m[0][j] == m[1][j] == m[2][j]:
            winner = m[0][j]
            wins += 1

    # diagonal check
    if m[0][0] == m[1][1] == m[2][2] or m[0][2] == m[1][1] == m[2][0]:
        winner = m[1][1]
        wins += 1

    if winner == '_' or winner == ' ':
        wins = 0
        return 1
    elif wins == 1:
        print(f"{winner} wins")
        return 0
    elif (no_of_element(m, ' ') == 0):
        print("Draw")
        return 0
    else:
        return 1


game_input = 'X'
game_continue = 1
change_input = 1
print_screen(matrix)

while game_continue == 1:

    matrix, change_input = input_element(matrix, game_input)
    game_continue = check_winner(matrix)

    if change_input == 0:
        if game_input == 'X':
            game_input = 'O'
        else:
            game_input = 'X'
