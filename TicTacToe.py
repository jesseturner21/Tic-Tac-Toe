class TicTacToe:
    rows, cols = (3, 3)
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def __init__(self):

        self.show_board()
        for i in range(9):
            if i % 2 == 0:
                player = 'X'
            else:
                player = 'O'

            location = input('\n' + player + ' select a location:')

            row = int(location[0])
            column = int(location[1])

            self.board[row][column] = player

            print()
            self.show_board()

            if i > 3:
                for r in range(self.rows):
                    if self.board[r][0] == self.board[r][1] == self.board[r][2]:
                        print('\n' + self.board[r][0] + ' IS THE WINNER!')
                        i = 8
                for c in range(self.cols):
                    if self.board[0][c] == self.board[1][c] == self.board[2][c]:
                        print('\n' + self.board[0][c] + ' IS THE WINNER!')
                        i = 8
                if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                    print('\n' + self.board[0][0] + ' IS THE WINNER!')
                    i = 8
                if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                    print('\n' + self.board[0][0] + ' IS THE WINNER!')
                    i = 8

    def show_board(self):
        print('    0   1   2')
        for r in range(self.rows):
            print(' ' + str(r) + '  ' + self.board[r][0] + ' | ' + self.board[r][1] + ' | ' + self.board[r][2] + '  ')
            if r != 2:
                print('   -----------')
