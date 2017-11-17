####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 10' # Only 10 chars displayed.
strategy_name = 'Ez winz'
strategy_description = 'It decides by trying to make collude 3 times then betraying'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    if 'c,b,b' in their_history [0:-3]:
        return 'c'
    if 'c,b,c' in their_history [0:-3]:
        return 'c'
    if 'c,c,c' in their_history [0:-3]:
        return 'b'
    if 'c,c,b' in their_history [0:-3]:
       return 'c'
    if 'c' in their_history [0:-1]:
        return 'c'
    if 'b' in their_history [0:-3]:
        return 'b'
    else:
        return 'c'
   
     

        
        
    
