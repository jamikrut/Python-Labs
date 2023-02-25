# chess_row = ["--" for i in range(8)]
# chess_board = [chess_row[:] for i in range(8)]
# print(chess_board)

WHITE_POWN = "WP"
BLACK_POWN = "BP"

chess_board = [["--" for i in range(8)] for i in range(8)]

chess_board[0][0] = WHITE_POWN
chess_board[3][5] = BLACK_POWN

for chess_row in chess_board:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()
