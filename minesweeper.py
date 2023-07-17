
empty=0
mine=1
unknown=-1
flag=-2



grid=[
    [0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,1,0,1,0],
    [0,0,1,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,1,0,0,0],
    [0,0,1,1,0,0,0,0,0]
]


player_grid=[
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],

]


def count():
    pass

def click(row,col):
    if grid[row][col]==mine:
        print("BOOM!")

def set_flag(row,col):
    if player_grid[row][col]==unknown:
        player_grid[row][col]=flag

    

def show_grid():
    symbols={-2:"F",-1:"."}
    for row in range (len(player_grid)):
        for col in range (len(player_grid[row])):    # we wrote [row] becouse  its col for the above particular row
          value=player_grid[row][col]                           #value is made to use row and col
          if value in symbols:
              symbol=symbols[value]
          else:
              symbol=str(value)    
          print(f"{symbol}",end='')                   # end='' prevents the print statement to go to the next line 
        print("")

#testing code
click(0,0)
set_flag(0,0)
# print(player_grid)
show_grid()
