#!/usr/bin/env python

import sys


class sudoku():

    def __init__(self, puzzle):

        self.puzzle = [int(v) for v in puzzle]

        #column_possibilities
        self.columns = [[x for x in range(1,10)] for i in range(9)]
        for index,value in enumerate(self.puzzle):
        # count (0-80) of the list, value = 1-9
            if value != 0:
                column = index%9
        #remainder of 9 is the column number
                self.columns[column].remove(value)


        #row_possibilities
        self.rows = [[x for x in range(1,10)] for i in range(9)]
        for index,value in enumerate(self.puzzle):
            if value !=0:
                row = index//9
                self.rows[row].remove(value)

        #block_possibilities
        self.blocks = [[x for x in range(1,10)] for i in range(9)]
        for index,value in enumerate(self.puzzle):
            block = 0
            if value !=0:
                row = index//9
                column = index%9
                block = int(row/3)*3 + int(column/3)
                self.blocks[block].remove(value)

    def __repr__(self):

         return "".join(str(x) for x in self.puzzle) + "\n"

    def __str__(self):

        s = "\n+---+---+---+"
        for block in range(3): # for each horizontal block
          for row in range(3): # for each row
            s += "\n|"
            for col in range(3): # for each vertical block
              # Horrible?  Perhaps: adding three characters
              # at a time, to the strings, followed by a pipe.
              s += "".join([str(v) for v in self.puzzle[block*27+row*9+col*3:block*27+row*9+col*3+3]]) + "|"
          s += "\n+---+---+---+" # after every full block, a line.

        return s

# verify_solution(): Write a method to check your solution. Try to check three conditions:
# The initial values should all be there. To check this, you'd need to somehow save a copy of the initial state of the puzzle, before you started working on it.
#There should be no zeroes left in the puzzle.
# Every row, column, and box should have exactly one of the digits 1-9.'''

    def verify_solution(self): # verifying is easy!!
        #Create empty lists
        columnsV = [[] for i in range(9)] 
        rowsV = [[] for i in range(9)]
        blocksV = [[] for i in range(9)]
        for index,value in enumerate(self.puzzle):
            column = index%9
            row = index//9
            block = self.get_box(index)
            #If value is not found in row, column, or block, add it
            #Else if value is already found in row,column or block, then sudoku is not solved
            if value not in columnsV[column]:
                columnsV[column].append(value)
            else:
                print("Column {} has duplicate {}, index{}".format(column,value, index))
                return False

            if value not in rowsV[row]:
                rowsV[row].append(value)
            else:
                print("Row {} has duplicate {}, index{}".format(row,value, index))
                return False

            if value not in blocksV[block]:
                blocksV[block].append(value)
            else:
                print("Block {} has duplicate {}, index{}".format(block,value, index))
                return False
        return True

## THESE ARE THE MEATY METHODS THAT ACTUALLY DO THINGS...

# Given the cell index, it's pretty easy to figure out the row (cell // 9) or column (cell % 9). The box is a little trickier. Write the method once, check it carefully, and call it when you need it.
    def get_box(self,index):
        row = index // 9
        column = index % 9
        box = int(row/3)*3 + int(column/3)
        return box

# Get the possibilities for the row, column, and box.
# Their intersection is the possibilities of the cell.
    def cell_possibilities(self):
        x = []
        for i in range(81):
            x.append([])
            if self.puzzle[i] == 0:
                row = i // 9
                column = i % 9
                block = self.get_box(i)
                for j in self.rows[row]:
                    if j in self.columns[column] and j in self.blocks[block]:
                        x[i].append(j)
        return x

    # Assign a cell to a value,
    # and remove the possibilities from the row, column, and box.
    def assign_cell(self,cell,value):
        #Edit self.puzzle, assign value to a cell
        self.puzzle[cell] = value
        #Now remove value from possibilities in row, column, block
        row = cell//9
        column = cell%9
        block = self.get_box(cell)
        self.rows[row].remove(value)
        self.columns[column].remove(value)
        self.blocks[block].remove(value)
        #print("Assigned {} to cell {}".format(value, cell)) #Shows assignment
        

    # Loop over the puzzle repeatedly,
    # searching for cells where only a single value is possible.
    # In those cases, assign the cell to that single value.
    # For sets, the easiest is s.pop(); for list, it's... the first element!!
    def assign(self):
        #Create list of unsolved indices
        unsolved = [i for i in range(len(self.puzzle)) if self.puzzle[i] == 0]
        terminate = 0 #In case problem is not solveable (more than 2 possibilities in all remaining cells)
        while unsolved and terminate < 100: #If solveable, at least one entry filled per loop, maximum 81 loops
            for index in unsolved: #Loop through all unsolved indices
                if len(self.cell_possibilities()[index]) == 1: #Assign cell value if only 1 possibility
                    value = self.cell_possibilities()[index][0]
                    self.assign_cell(index,value)
                    unsolved.remove(index) #Update list of unsolved indices
            terminate += 1  
        
  ## Go on... try recursion!  It's fun!!

solved, total = 0, 0
with open("sudoku_solved_easier.txt", "w") as out:
  for line in open("sudoku_easier.txt"):

    p = line.strip()
    s = sudoku(p)
    s.assign()
    print(s)
#    break

    total += 1
    if s.verify_solution(): solved += 1

    out.write(s.__repr__())

print("Easy {}/{} = {:.3f}".format(solved, total, solved/total))
