    def cell_possibilities():
        self.cell_possibilities = [[x for x in range(1,10)] for i in range(9)]
        for index,value in enumerate(self.puzzle):
            if value != 0:
                row = index//9
                column = index%9
                block = int(row/3)*3 + int(column/3)
                self.cell_possibilities[block].remove(value)
                self.cell_possibilities[row].remove(value)
                self.cell_possibilities[column].remove(value)
        print(self.cell_possibilities)
        return


line = '''001700509573024106800501002700295018009400305652800007465080071000159004908007053'''
bulba = sudoku(line)
y = bulba.cell_possibilities()
print(y)

#!/usr/bin/env python

import sys


class sudoku():

    def __init__(self, puzzle):

        self.puzzle = [int(v) for v in puzzle]

        # Save a copy to check our work, later.

        # Initialize the 'unassigned' lists.
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
                block = (index//27)*27 + 3*(index%9//3)
                self.blocks[block].remove(value)
        print(self.blocks)
  #######
  # CHECKS AND PRINTING

    def __repr__(self):

         return "".join(str(x) for x in self.puzzle) + "\n"


      # Print method, hopefully makes it
      # it easier to understand and grapple
      # with the algorithm.

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

    def verify_solution(self): # verifying is easy!!
        if self.rows == 0:
            return("error! zero value found in row")
        if self.columns == 0:
            print("error! zero value found in column")
        if self.blocks == 0:
            print("error! zero value found in block")
    #   print(self.puzzle is self.puzzle)
    #        print("error! original puzzle modified")

    # verify if there is any zero
    # have you altered the puzzle
    # class for inital puzzle
#        print("Could be!  Let's just say yes!!")
#        return True


      ## THESE ARE THE MEATY METHODS THAT ACTUALLY DO THINGS...

    def get_box(self, cell):
        return 0

      # Get the possibilities for the row, column, and box.
      # Their intersection is the possibilities of the cell.
    def cell_possibilities(self, index):
        print(self)
        x = []
        print(self.rows)
        print(self.columns)
        print(self.blocks)
        for self.rows in self.columns and self.rows in self.blocks:
            x.append(self.rows)
        print(x)
        pass
#       [i for i in self.rows if not(i in self.column)]




    # Assign a cell to a value,
    # and remove the possibilities from the row, column, and box.
    def assign_cell(self, cell, value):
        while 0 in self.puzzle:
            for index,value in enumerate(puzzle):
                if value !=0:
                    continue
                cp = self.cell_possibilities(index)
                if len(cp) == 1:
                    self.puzzle[index] = value
                    self.rows[row].remove(value)
                    self.columns[column].remove(value)

        pass


    # Loop over the puzzle repeatedly,
    # searching for cells where only a single value is possible.
    # In those cases, assign the cell to that single value.
    # For sets, the easiest is s.pop(); for list, it's... the first element!!
    def assign(self):

        pass


  ## Go on... try recursion!  It's fun!!



solved, total = 0, 0
with open("sudoku_solved_easier.txt", "w") as out:
  for line in open("sudoku_easier.txt"):

    p = line.strip()
    s = sudoku(p)
    s.assign()
    print(s)

    total += 1
    break
    cif s.verify_solution(): solved += 1

    out.write(s.__repr__())

print("Easy {}/{} = {:.3f}".format(solved, total, solved/total))
