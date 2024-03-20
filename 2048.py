import numpy
import random

class Play2048:
    # Command Functions
        # commands:
        # 0: new game
        # 1: load game.
        # 2: save game.
        # 3: screenshot board (w/ timestamp)
        # 4: high score list
        # 5: clear saved data

    def Command(self):
        command = input("Please enter command: ")
        command = str(command)
        command.strip()
        if command == "0":
            Play2048.NewGame(self)
        elif command == "1":
            Play2048.LoadGame(self)
        elif command == "2":
            Play2048.SaveGame(self)
        elif command == "3":
            Play2048.ScreenShotBoard(self)
        elif command == "4":
            Play2048.ShowHighScore(self)
        elif command == "5":
            Play2048.ClearSavedData(self)
    
    def ScreenShotBoard(self):
        print()
    
    def ShowHighScore():
        print()

    def ClearSavedData():
        print()

    # Game Functions
    def Play(self, board):
        status = True
        while status == True:
            Play2048.PrintBoard(self,board)
            Play2048.Move(self, board)
            Play2048.PopulateBoard(self, board, 2)

    def NewGame(self):

        board = numpy.array([[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]])

        Play2048.PopulateBoard(self, board, 2)
        Play2048.PopulateBoard(self, board, random.choice([2,4]))
        Play2048.Play(self, board)

    def LoadGame(self):
        print()

    def SaveGame(self):
        print()
    
    def Move(self, board):
        status = True        
        while status == True:
            move = input(": ")
            move = move.strip()
            move = move.upper()
            if move == "W" or move == "A" or move == "S" or move == "D":
                status = False
            else:
                print("Invalid move. Acceptable moves are W (up), A (left), S (down), and D (right).")

        Play2048.UpdateBoard(self, board, move)

    def PushRight(self, board):
        # push everything to the right
        for row in range(0,4):
            for col in range(0,3):
                if board[row][col+1] == 0:
                    board[row][col+1] = board[row][col]
                    board[row][col] = 0

        # if there are corresponding pairs, combine them
        for row in range(0,4):
            for col in range(0,3):
                if board[row][col] == board[row][col+1]:
                    board[row][col+1] = 2*board[row][col]
                    board[row][col] = 0
                    break

        for row in range(0,4):
            col = 3
            while col >= 0:
                if board[row][col] == board[row][col-1]:
                    board[row][col] = 2*board[row][col]
                    board[row][col-1] = 0
                    break
                col -= 1
        
        for row in range(0,4):
            for col in range(0,3):
                if board[row][col+1] == 0:
                    board[row][col+1] = board[row][col]
                    board[row][col] = 0

        return board

    def CheckIfLost(self, board):
        print()

    # Board Functions
    def PrintBoard(self, board):
        print("\n")
        for i in range(0,4):
            for j in range(0,4):
                print("a")
                # print(board[i][j], end=" ")
            # print("\n")
    
    def PopulateBoard(self, board, value = 2):
        """
        Add to an random empty square a value, by default 2. 
        """
        square = Play2048.SelectRandomSquare(self, board)

        board[square[0]][square[1]] = value

    def SelectRandomSquare(self, board):
        status = True
        while status == True:
            coord1 = random.randrange(0,4)
            coord2 = random.randrange(0,4)
            if board[coord1][coord2] != 0:
                continue
            elif board[coord1][coord2] == 0:
                return [coord1, coord2]
            else:
                exit()

    def UpdateBoard(self, board, move):
        if move == "W":
            board = numpy.rot90(board, 3)
            board = Play2048.PushRight(self, board)
            board = numpy.rot90(board, 1)
        elif move == "A":
            board = numpy.rot90(board, 2)
            board = Play2048.PushRight(self, board)
            board = numpy.rot90(board, 2)
        elif move == "S":
            board = numpy.rot90(board, 1)
            board = Play2048.PushRight(self, board)
            board = numpy.rot90(board, 3)
        elif move == "D":
            # don't rotate
            board = Play2048.PushRight(self, board)
        else:
            exit()
        return board

    def ScreenShotBoard():
        print()
        

# board = numpy.array([[0,1,1,1],
#         [1,1,1,1],
#         [1,1,1,1],
#         [1,1,1,1]])

# board 
# = numpy.array([[0,1,1,1],
#         [1,1,1,1],
#         [1,1,1,1],
#         [1,0,0,0]])

board = numpy.array([[0,2,2,4],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]])

game = Play2048()

game.Play(board)

# game.NewGame()

# Command Loop

status = True
# while status == True:
#     game.Command()