def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(
            board[j][i] == player for j in range(3)
        ):
            return True

    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def x0():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            row = int(input("Введите номер строки (1, 2, 3): ")) - 1
            col = int(input("Введите номер столбца (1, 2, 3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = current_player

                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Игрок {current_player} выиграл!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("Ничья!")
                    break

                current_player = "O" if current_player == "X" else "X"

            else:
                print(
                    "Эта ячейка уже занята или указаны неверные координаты."
                )
        except ValueError:
            print("Ошибка ввода")


x0()
