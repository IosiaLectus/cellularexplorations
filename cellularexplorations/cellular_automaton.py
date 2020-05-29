#!/usr/bin/env python

# import useful packages
import random



def lookup_table_from_wolfram_code(num_nbhd_states, wolfram_code):
    '''
    Takes a Wolfram code, and converts it into a list lookup_table, such that if the state of a cell's neighborhood is encoded by the integer x, then lookup_table[x] gives the updated state of the cell. 
    '''
    # Place holder:
    return [0 for i in range(num_nbhd_states)]

class CellularAutomaton1D:
    '''
    This is a class for defining a one dimensional cellular automaton.
    '''

    def __init__(self, width, wolfram_code, neighborhood_radius=1, num_states=2, periodic=True):
        '''
        Initializes a one dimensional cellular automaton on a line if width 'width'. The rule of the automaton is set by the Wolfram code specified in in wolfram_code. 'neighborhood_radius' sets the size of a neighborhood. For example, neighborhood_radius=1 results in nearest neighbor neighborhoods, and neighborhood_radius=2 results in neighborhoods that also include next nearest neighbors. 'num_states' defines the number of states a cell may take, the default being 2. 'periodic' determines whether the boundary conditions are periodic. If they are not periodic, the boundary condition will be that there exit two additional cells whose state is always zero. 
        '''
        # The total number of states each cell can take
        self.num_states = num_states
        self.nbhd_radius = neighborhood_radius
        # The number of cells in each neighborhood
        self.nbhd_size = (2*self.nbhd_radius)+1
        # The number of states a neighborhood can take
        self.num_nbhd_states = self.num_states**self.nbhd_size
        # The maximum wolfram code, which coincides with the number of unique local rules.
        self.maximum_wolfram_code = self.num_states**self.num_nbhd_states
        self.is_periodic = False
        self.grid_width = width
        # self.grid will be a list which stores the state of each cell. If the boundary condition is aperiodic, we include a number of additional cells equal to the neighborhood radius. In that case the last 'self.nbhd_radius' number of cells will not evolve. 
        if self.is_periodic:
            self.grid = [0 for i in range(self.grid_width)]
        else:
            self.grid = [0 for i in range(self.grid_width+self.nbhd_radius)]
        # Check that the Wolfram code provided makes sense:
        assert wolfram_code>=0 and wolfram_code<=self.maximum_wolfram_code, 'Invalid Wolfram code.'
        # self.rule_dict is a dictionary which gives a lookup table for every active wolfram code.
        self.rule_dict = {}
        self.rule_dict[wolfram_code] = lookup_table_from_wolfram_code(self.num_nbhd_states, wolfram_code)
        # self.rule_grid stores the Wolfram code which applies to each individual cell. This allows one to partition the grid into regions governed by different rules, which could lead to interface effects.
        self.rule_grid = [wolfram_code for i in range(self.grid_width)]

    def lookup_table_from_wolfram_code(self, wolfram_code):
        '''
        Takes a Wolfram code, and converts it into a list lookup_table, such that if the state of a cell's neighborhood is encoded by the integer x, then lookup_table[x] gives the updated state of the cell. 
        '''
        # Place holder:
        return [0 for i in range(self.num_nbhd_states)]

    def update_rule_global(self, wolfram_code):
        '''
        Updates the rule globally base on 'wolfram_code'.
        '''
        self.rule_dict = {wolfram_code: lookup_table_from_wolfram_code(self.num_nbhd_states, wolfram_code)}
        self.rule_grid = [wolfram_code for i in range(self.grid_width)]

    def update_rule_local(self, wolfram_code, index):
        '''
        Updates the rule of a single cell whose index is given by 'index'.
        '''
        self.rule_dict.update({wolfram_code, lookup_table_from_wolram_code(self.num_nbhd_states, wolfram_code)})
        self.rule_grid[index] = wolfram_code

    def set_state_local(self, index, state):
        assert state>=0 and state<=self.num_states, 'Invalid state'
        self.grid[index] = state


    def get_neighborhood_state(self, index):
        '''
        Returns the encoded state of the neighborhood of the cell at index 'index'.
        '''
        # Get the slice of self.grid that corresponds to the neighborhood in question
        if self.is_periodic:
            nbhd_slice = [self.grid[(self.grid_width + index - self.nbhd_radius + i)%self.grid_width] for i in range(self.nbhd_size)]
        else:
            nbhd_slice = [self.grid[index-self.nbhd_radius+i] for i in range(self.nbhd_size)]
        # get the base 'num_states' digits of state
        digits = [nbhd_slice[i]*(self.num_states**i) for i in range(len(nbhd_slice))]
        return sum(digits)



    def step(self):
        '''
        Do a single time step, i.e. update the state of the cellular automaton once.
        '''
        new_grid = [0 for i in range(len(self.grid))]
        for i in range(self.grid_width):
            new_grid[i] = self.rule_dict[self.rule_grid[i]][self.get_neighborhood_state(i)]
        self.grid = new_grid



class CellularAutomaton2D:
    '''
    This is a class for defining a two dimensional cellular automaton on a square grid.
    '''

class CellularAutomatonHex:
    '''
    This is a class for defining a two dimensional cellular automaton on a hex grid.
    '''

def main():
    print("Hello world\n")
    aut = CellularAutomaton1D(20,32)
    aut.set_state_local(12,1)
    print(aut.grid)
    for i in range(30):
        aut.step()
        print(aut.grid)
    print()

if __name__ == '__main__':
    main()
