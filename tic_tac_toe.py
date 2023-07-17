from operator import truediv


board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]
user= True  #to toggle  #when true it refers to x and when false it refers to o
turns =0
def print_board(board):
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()


print_board(board)    


def quit(user_input):
  if user_input.lower() == "q": 
    print("Thanks for playing")
    return True
  else: return False


def check_input(user_input):
  if not is_num(user_input): return False
  user_input = int(user_input)
  if not bounds(user_input): return False
  return True


def is_num(user_input):
  if not user_input.isnumeric():
    print("this is not a valid number")
    return False
  else: return True 

def bounds(user_input):
  if user_input > 9 or user_input <1:
    print("This number is out of bounds")
    return False
  else: return True

def is_taken(coords,board):
  row = coords[0]
  col = coords[1]
  if board[row][col] !="-":
    print("This place is already occupied")
    return True
  else: return False

def coordinates(user_input):
  row = int(user_input / 3)
  col = user_input
  if col > 2: col = int(col % 3)
  return (row,col)


def add_to_board(coords,board,active_user):
  row=coords[0]
  col=coords[1]
  board[row][col]=active_user


def current_user(user):
  if user: return "x"
  else: return "o"


def iswin(board,user):
  if check_row(board,user): return True
  if check_col(board,user): return True
  if check_diag(board,user): return True
  return False



def check_row(user, board):
  for row in board:
    complete_row = True
    for slot in row:
      if slot != user:
        complete_row = False
        break
    if complete_row: return True
  return False 

def check_col(user, board):
  for col in range(3):
    complete_col = True
    for row in range(3):
      if board[row][col] != user:
        complete_col = False
        break
    if complete_col: return True
  return False  

def check_diag(user,board):
 if board[0][0]== user and board[1][1]== user and board[2][2]==user : return True   #from top left to bottom right
 elif  board[0][2]== user and board[1][1]== user and board[2][0]==user : return True   #from top right to bottom left
 else: return False


while turns<9 :
  active_user=current_user(user)
  print_board(board)
  user_input=input("please enter a valid number through 1 to 9 or press \"q\" to quit: ")
  if quit(user_input): break
  if not check_input(user_input):
    print("please try again")
    continue
  user_input = int(user_input)-1            #because arrays are indexed at 0 therefore it should be one less 
  coords = coordinates(user_input)
  if is_taken(coords,board):
    print("please try again ")
    continue
  add_to_board(coords,board,active_user)
  user = not user
  if iswin(active_user,board):
    print(f"{active_user.upper()} won!!")
    break
  turns += 1
  if turns ==9 : print("Its a tie!")