from random import randrange
# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# latest stats
# w/ random
# game 1: 48%
# game 2: 52%
# game 3: 49%
# game 4: 50%
# w/ Strategy #1
# game 1: 74% !!!
# game 2: 39%
# game 3: 50%
# game 4: 85% !!!
# w/ S1 and S2
# game 1: 74% !!!
# game 2: 50%
# game 3: 49%
# game 4: 84% !!!

def player(prev_play, opponent_history=[], my_history=[], wins_and_losses={'W': 0, 'L': 0}):
    opponent_history.append(prev_play)
    next_moves = {'R': {}, 'P': {}, 'S': {}}
    guess = "R"

    if prev_play:
      # Strategy #1: get probability of next move of opponent
      if len(opponent_history) > 2:
        for key in next_moves:
          for i, mv in enumerate(opponent_history):
            if mv == key and len(opponent_history) > i + 1:
              next = opponent_history[i + 1]
    
              if next != '':
                if next in next_moves[key].keys():
                  next_moves[key][next] += 1
                else:
                  next_moves[key][next] = 1
    
        pp_dict = next_moves[prev_play]
  
        if pp_dict:
          max_move = max(pp_dict, key=pp_dict.get)
          
          if max_move == 'R':
            guess = 'P'
          elif max_move == 'P':
            guess = 'S'
          else:
            guess = 'R'

      # keep track of my own win rate
      last_game = my_history[-1] + prev_play
      if last_game == 'RP':
        wins_and_losses['L'] += 1
      elif last_game == 'RS':
        wins_and_losses['W'] += 1
      elif last_game == 'PS':
        wins_and_losses['L'] += 1
      elif last_game == 'PR':
        wins_and_losses['W'] += 1
      elif last_game == 'SR':
        wins_and_losses['L'] += 1
      elif last_game == 'SP':
        wins_and_losses['W'] += 1

    if len(opponent_history) % 1000 == 0:
      wins_and_losses['W'] = 0
      wins_and_losses['L'] = 0

    if len(opponent_history) > 100 and wins_and_losses['L'] > wins_and_losses['W']:
      # im getting BTFO! change strategies
      # Strategy #2: random
      rand_index = randrange(0, 3)
      guess = list(next_moves.keys())[rand_index]
  
    my_history.append(guess)
  
    return guess
