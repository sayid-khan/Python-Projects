
from tkinter import Button,Label
import random
from typing import Counter
import ctypes    #used to throw generic message box or alert
import sys


cell_count1=36

class Cell:
    all=[]
    cell_count=cell_count1
    cell_count_lablel_object=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.is_opened=False
        self.is_mine_candidate= False
        self.cell_btn_object=None
        self.x=x
        self.y=y
        # append the object to the cell.all list
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn=Button(
            location,
            width=11,
            height=3,
            
        )
        btn.bind('<Button-1>',self.left_click_actions)     #for left click button-1 is used 
        btn.bind('<Button-3>',self.right_click_actions)     #for right click button-3 is used 
        self.cell_btn_object=btn

    @staticmethod     #just to use the class and not the instance/object
    def create_cell_count_lablel(location):
        lbl= Label(
            location,
            text=f"cells_left:{Cell.cell_count}",
            font=("",24),     #""is the font type
            bg='black',
            fg='white'
        )
        Cell.cell_count_lablel_object=lbl




    def left_click_actions(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cell_mine_len==0:
                for cell_obj in self.surround_cells:
                    cell_obj.show_cell()
            self.show_cell()
            #if mmines count is equal to number of cells
            #left, player won
            if Cell.cell_count==9:
                ctypes.windll.user32.MessageBoxW(0,'You clicked On a Mine','Game Over',0)

                

          #cancel left and right click event 
          # if cell is already opened  
            self.cell_btn_object.unbind('<Button-1>')
            self.cell_btn_object.unbind('<Button-3>')

    def show_cell_axis(self,x,y):
        # return a cell object based on the of x and y
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell

    @property    #to create an attribute to make it read only
    def surround_cells(self):
        cells=[                    #[] means list
            self.show_cell_axis(self.x - 1,self.y - 1),
            self.show_cell_axis(self.x - 1,self.y),
            self.show_cell_axis(self.x - 1,self.y + 1),
            self.show_cell_axis(self.x ,self.y - 1),
            self.show_cell_axis(self.x + 1,self.y - 1),
            self.show_cell_axis(self.x + 1,self.y),
            self.show_cell_axis(self.x + 1,self.y + 1),
            self.show_cell_axis(self.x,self.y + 1)

        ]     

        cells=[cell for cell in cells if cell is not None ] 
        return(cells)

    

    @property
    def surrounded_cell_mine_len(self):      #it will calculate the number of mines in the surrounding mines when a cell is clicked   
        Counter=0
        for cell in self.surround_cells:
            if cell.is_mine:
                Counter+=1

        return Counter      

    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -=1
            self.cell_btn_object.configure(text=self.surrounded_cell_mine_len)
            if Cell.cell_count_lablel_object:
                Cell.cell_count_lablel_object.configure(
                    text= f"cells_left:{Cell.cell_count}"
                )
            
        #if this was a mine candidate then for safety configure
        # the background color back to systembuttonface
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )

        #mark the cell as opened (use it as the last line of this method)        
        self.is_opened=True        
        

    def show_mine(self):
        #a logic to interrupt and show that the player has lost the game
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'You clicked On a Mine','Game Over',0)
         # numbers 0 & 0 are for buttons we can also try other combinations 0 & 2
        sys.exit()         # to terminate game on pressing ok

    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate= True
        else:
            self.cell_btn_object.configure(
                bg='systembuttonface'
            )
            self.is_mine_candidate=False

    @staticmethod
    def randomize_mines():
        picked_cells=random.sample(
            Cell.all,9
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine= True


    def __repr__(self):
        return f"({self.x},{self.y})"