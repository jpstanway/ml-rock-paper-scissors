# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# latest stats
# w/ Strategy #1
# game 1: 20%
# game 2: 3%
# game 3: 0%
# game 4: 0%
# w/ Strategy #2
# game 1: 74%
# game 2: 39%
# game 3: 50%
# game 4: 84%

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = "R"

    # Strategy #1: default strategy (random)
  
    # Strategy #2: get probability of next move of opponent
    next_moves = {'R': {}, 'P': {}, 'S': {}}

    if prev_play and len(opponent_history) > 10:
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
        most_likely_next_move = max(pp_dict, key=pp_dict.get)

        if most_likely_next_move == 'R':
          guess = 'P'
        elif most_likely_next_move == 'P':
          guess = 'S'
        else:
          guess = 'R'
          
    # Strategy #3: get most used move of opponent

    return guess
