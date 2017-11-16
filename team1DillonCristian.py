import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Safety' # Only 10 chars displayed.
strategy_name = 'We believe that safety is the only thing that matters.'
strategy_description = 'We like to backstab people only if they lodge a knife into our backs.'
    
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
    c = 0
    b = 0
    
    if len(my_history)==0: # The first time the choice will be randomized
        return random.choice(['b', 'c']) # Choice between 'b' and 'c'
    else:
        for i in their_history: # Created a FOR loop
            if i == 'b': # If i is equal to 'b'
                b = b + 1 # add one to the variable b
            else: # If i is not equal to 'b'
                c = c + 1 # Add one to the variable c
        if my_score < their_score: # If my score is less than their score
            if b > c: # If variable b is greater than variable c (Basically saying 'if 'b' shows up more than 'c')
                return random.choice(['b', 'b', 'b', 'b', 'c']) # Return 'b' most likely but once in a while choose 'c'
            else: # If variable c is greater than variable b (Basically saying 'if 'c' shows up more than 'b')
                return random.choice(['c', 'c', 'c', 'c', 'b']) # Return 'c' most likely but once in a while choose 'b'
        else: 
            if 'bbbbb' in their_history[-10:0]:
                if b > c:
                    return random.choice(['b', 'b', 'b', 'b', 'c']) # Returns 'b' most likely but once in a while choose 'c'
            else: # If less than 5 'b's are in the previous 10
                if 'bbbb' in their_history[-10:0] or 'bbb' in their_history[-10:0]:
                    if b < c: # If they've got three 'b's within the last ten and if they've selected 'b' less than 'c'
                        return random.choice(['b', 'c', 'c', 'b', 'c']) # Returns 'c' probably but sometimes chooses 'b'
                    else: # If they've got three 'b's within the last ten and if they've selected 'b' more than 'c'
                        return random.choice(['b', 'b', 'c', 'b', 'c']) # Returns 'b' probably but sometimes chooses 'c'
                else: # If they've got less than 3 'b's within the last ten
                    if b > c: # If betray is greater than collude overall
                        return random.choice(['b', 'c']) # Returns 'c' probably but sometimes chooses 'b'
                    else: # If betray is less than collude overall
                        return random.choice(['b', 'c', 'c'])

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbccbbbcccbbbb',
              their_history='cccbbbcccbcbcb', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=100, 
              their_score=0,
              result='')             