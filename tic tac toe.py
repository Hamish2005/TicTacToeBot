X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    print(
    """
    welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    this will be a great showdown bettewen your human brain and my silicon prossor.

    you will make your move known by entering a number, 0 -8. the number will
    correspond to the board position  as illustrated:

                  0 | 1 | 2
                  ----------
                  3 | 4 | 5
                  ----------
                  6 | 7 | 8
                  
    prepare yourself, living creature. the ultimate battle is about to begin
    """
    )
    
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. you will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your failure you are a very low iq living creature ... i will go first.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    for i in range(0, len(board) // 3):
        i = i * 3
        print(board[i] + " | " + board[i + 1] + " | " + board[i + 2])
        if (len(board) > i + 3):
            print("----------")

def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nYou living creature your iq is to little for to to play a game of this high calabur you incompititent living creature this square is taken. chosse another square you bot.|n")
    print("Fine...")
    return move

def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best postiions to have, in order
    BEST_MOVES = (0, 8, 6, 2, 3, 7, 4, 5, 1)

    print("i shall take square number", end=" ")

    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    
    # since there is no winner  pick best square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
    
        
        
def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("it's a tie!\n")

    if the_winner == computer:
        print("As i perdicted you un-cultured swine you loss to my supereme abialtly you stale baguette")

    elif the_winner == human:
        print(" a software malufunction error now why you horenduse human hacking my mainframe")

    elif the_winner == TIE:
         print(" the proablity of you winning is 0.000001% the odds of tieing is 1% i see you have extreme luck")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# start the program
main()

