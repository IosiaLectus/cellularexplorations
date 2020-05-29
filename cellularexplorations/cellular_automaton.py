#!/usr/bin/env python

# import useful packages
import random

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
        self.nbhd_radius = negihborhood_radius
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
        self.rule_dict = {wolfram_code: lookup_table_from_wolfram_code(wolfram_code)}
        # self.rule_grid stores the Wolfram code which applies to each individual cell. This allows one to partition the grid into regions governed by different rules, which could lead to interface effects.
        self.rule_grid = [wolfram_code for i in range(self.grid_width)]

    def lookup_table_from_wolfram_code(wolfram_code):
        '''
        Takes a Wolfram code, and converts it into a list lookup_table, such that if the state of a cell's neighborhood is encoded by the integer x, then lookup_table[x] gives the updated state of the cell. 
        '''
        # Place holder:
        return [0 for i in range(self.num_nbhd_states)]

    def update_rule_global(wolfram_code):
        '''
        Updates the rule globally base on 'wolfram_code'.
        '''
        self.rule_dict = {wolfram_code: lookup_table_from_wolfram_code(wolfram_code)}
        self.rule_grid = [wolfram_code for i in range(self.grid_width)]

    def update_rule_local(wolfram_code, index)
        '''
        Updates the rule of a single cell whose index is given by 'index'.
        '''
        self.rule_dict.update({wolfram_code, lookup_table_from_wolram_code})
        self.rule_grid[index] = wolfram_code

    def get_neighborhood_state(index):
        '''
        Returns the encoded state of the neighborhood of the cell at index 'index'.
        '''

    def step():
        '''
        Do a single time step, i.e. update the state of the cellular automaton once.
        '''



class CellularAutomaton2D:
    '''
    This is a class for defining a two dimensional cellular automaton on a square grid.
    '''

class CellularAutomatonHex:
    '''
    This is a class for defining a two dimensional cellular automaton on a hex grid.
    '''
