#!/usr/bin/env python

# import useful packages
import tkinter as tk
import cellular_automaton, math


def state_to_color(color):
    state_to_color_dict = {0:'white', 1:'black', 2:'red', 3:'green', 4:'blue'}
    if color in state_to_color_dict.keys():
        return state_to_color_dict[color]
    return 'grey'

class CellGrid:
    '''
    This class will store the grid of cells and related graphical components for displaying our cellular automata.
    '''

    def __init__(self, root, width, height, dx):
        self.spacing = dx
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(root, width=self.width*self.spacing, height=self.height*self.spacing)
        self.canvas.bind('<Button-1>',self.on_click)
        self.canvas.pack()
        self.state_grid = [[0 for y in range(height)] for x in range(width)]
        self.grid = [[None for y in range(height)] for x in range(width)]
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = self.canvas.create_rectangle(x*self.spacing, y*self.spacing, (x+1)*self.spacing, (y+1)*self.spacing, fill='white')

    def on_click(self, event):
        grid_x = math.floor(event.x/self.spacing)
        grid_y = math.floor(event.y/self.spacing)
        self.toggle_cell(grid_x, grid_y, 5)

    def reset(self):
        '''
        Resets the grid
        '''
        self.state_grid = [[0 for y in range(height)] for x in range(width)]
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = self.canvas.create_rectangle(x*self.spacing, y*self.spacing, (x+1)*self.spacing, (y+1)*self.spacing, fill='white')

    def set_cell(self, x, y, state):
        self.state_grid[x][y] = state
        color = state_to_color_state
        self.canvas.itemconif(self.grid[x][y], fill=color)

    def toggle_cell(self, x, y, num_states=2):
        self.state_grid[x][y] = (self.state_grid[x][y]+1)%num_states
        self.canvas.itemconfig(self.grid[x][y], fill=state_to_color(self.state_grid[x][y]))



# actually do stuff:
def main():
    '''
    This is a docstring for the main function
    '''
    width = 100
    height = 50
    spacing = 25

    auto = cellular_automaton.CellularAutomaton1D(width, 30)

    # create a tk root widget
    tk_root = tk.Tk()

    # window header
    tk_header = tk.Label(tk_root, text='Cellular Explorations')
    tk_header.pack()
    # a cell grid object
    CellGrid(tk_root, width, height, spacing)

    tk_root.mainloop()


if __name__ == '__main__':
    main()
