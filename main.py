player_1_simbol = "X"
player_2_simbol = "O"

game_state = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

'''
  output:
    [0 0 0]
    [0 0 0]
    [0 0 0]

    OR

    [1 0 0]
    [0 1 0]
    [0 2 1]
'''
def print_game_state(game_matrix: list[list]) -> None:
  for row in game_matrix:
    print('[', end='')
    for element in row:
      print(element, end=' ')
    print(']')


def check_box(game_matrix, line_number, col_number, marker):
  row = game_matrix[line_number]
  row[col_number] = marker

def moves(matrix):
  row = -1
  col = -1
  while not valid_moves(matrix, row, col):
    row = int(input('Choose row 0, 1, 2: '))
    col = int(input('Choose collumn 0, 1, 2: '))
  return row, col
 

def valid_moves(game_matrix, row, col):
  return 0 <= row < 3 and 0 <= col < 3 and game_matrix[row][col] == 0


def player_move(game_matrix, player, row, col):
  game_matrix[row][col] = player


def is_final_state(game_matrix):
  for row in game_matrix:
    if row[0] == row[1] and row[1] == row[2] and row[0] != 0:
      return True 
  for collumn in range (0,2):
    if game_matrix[0][collumn] == game_matrix[1][collumn] and game_matrix[1][collumn] == game_matrix[2][collumn] and game_matrix[0][collumn] != 0:
      return True
  if game_matrix[0][0] == game_matrix[1][1] and game_matrix[1][1] == game_matrix[2][2] and game_matrix[0][0] != 0:
    return True
  if game_matrix[0][2] == game_matrix[1][1] and game_matrix[1][1] == game_matrix[2][0] and game_matrix[0][2] !=0:
    return True
  

def Is_draw(game_matrix):
  for row in game_matrix:
    for element in row:
      if element == 0:
        return False
  return True    



Its_Player_1_Turn = False
while not is_final_state(game_state) and not Is_draw(game_state):
  Its_Player_1_Turn = not Its_Player_1_Turn
  print_game_state(game_state)
  if Its_Player_1_Turn:
    print('Player one make your choice!!!!!!!!')
  else:
    print("Player 2 make your move!!!!!!!!!")
  row, collumn = moves(game_state)
  symbol = player_1_simbol if Its_Player_1_Turn else player_2_simbol
  check_box(game_state, row, collumn, symbol)
  
if Is_draw(game_state):
  print("Its a draw :(")
elif Its_Player_1_Turn:
  print("player one won?!?!?!?!")
else:
  print("Player two won>><><><")