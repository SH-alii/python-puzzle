def get_tic_tac_toe_winner(game_play: list[list[str]] )-> str | None:
    
    for rown in game_play:
        if(rown[0] == rown[1] == rown[2] and rown[0] != ''):
            return 'winner is ' + rown[0]
        
    for column in range(3):
        if(game_play[0][column] == game_play[1][column] == game_play[2][column] and game_play[0][column] != ''):
            return 'winner is ' + game_play[0][column]
        
    if game_play[0][0] == game_play[1][1] == game_play[2][2] and game_play[0][0] != ' ':
        return 'winner is ' + game_play[0][0]
    if game_play[0][2] == game_play[1][1] == game_play[2][0] and game_play[0][2] != ' ':
        return 'winner is ' + game_play[0][2]
    
    return None
    
    
    
    
    
    
    
    
    



print(get_tic_tac_toe_winner([["X", "O", "O"], ["O", "X", "O"], ["X", "O","X"]]))