from turtle import width

def display_board(x,y,game_board, player_icon):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    game_board[x][y] = player_icon
    for element in range(len(game_board)):
           print(' '.join(game_board[element]))
