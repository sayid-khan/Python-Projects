from cProfile import label
from tkinter import *
from cell import Cell

root= Tk()                         #root is just a variable #Tk is used to create  a window #we take root beacuse it is mostly used in tkinter projects
root.configure(bg="black")
root.geometry('720x480')
root.title("Minesweeper Game")
root.resizable(False,False)       #to not resize the window #one false for width and one for height


top_frame=Frame(
    root,
    bg="black",    #change back to black
    width=720,
    height=120,
)
top_frame.place(x=0,y=0)

game_title=Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper',
    font=('',48)
)

game_title.place(x=180,y=0)

left_frame=Frame(
    root,
    bg="black",  #change back to black
    width=180,
    height=360,
)
left_frame.place(x=0,y=120)

centre_frame=Frame(
    root,
    bg="green",   #change back to black
    width=540,
    height=360,

)
centre_frame.place(x=180,y=120)



grid_size=6

for x in range(grid_size):
    for y in range(grid_size):
     c = Cell(x,y)
     c.create_btn_object(centre_frame)
     c.cell_btn_object.grid(
         column=x,row=y
    )


#call the label from the cell class
Cell.create_cell_count_lablel(left_frame)
Cell.cell_count_lablel_object.place(x=0,y=50)

Cell.randomize_mines()


#run the window
root.mainloop()                    #enable exit button 