#!/usr/bin/env python

import sys

class sudoku():

    def __init__(self, puzzle):

        self.initial_puzzle = [int(v) for v in puzzle]

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
    # Every row, column, and box should have exactly one of the digits 1-9.'''

    def verify_solution(self): # verifying is easy!!
        if self.puzzle == 0:
            return False #There should be no zeroes left in the puzzle.

    #every row should have exactly one of the digits 1-9.
        verify_digits = [i for i in range(1,10)]
        a = 0
        while a <= 72:
            x = sorted(self.puzzle[a:a+9])
            if x == verify_digits:
                return True
            else:
                return False
            a += 9
    # every column should have exactly one of the digits 1-9.
        b = 0
        print(index,value in enumerate(self.puzzle))
        for index,value in enumerate(self.puzzle):
            while b <= 9:
                b += 1
                if value != 0:
                    y = []
                    column = index%9
                    if column == b:
                        y.append(value)
                    sorted_column = sorted(y)
                    if sorted_column == verify_digits:
                        return True
                    else:
                        return False
    # every block should have exactly one of the digits 1-9.
        c = 0
        for index,value in enumerate(self.puzzle):
            while c <= 9:

                if value != 0:
                    z = []
                    block = get_box(index)
                    print(block)
                    if block == c:
                        z.append(value)
                    sorted_block = sorted(z)
                    c += 1
                    if sorted_block == verify_digits:
                        return True
                    else:
                        return False

        return

    ## THESE ARE THE MEATY METHODS THAT ACTUALLY DO THINGS...

    # Given the cell index, it's pretty easy to figure out the row (cell // 9) or column (cell % 9). The box is a little trickier. Write the method once, check it carefully, and call it when you need it.
    def get_box(self,index):
        row = index//9
        column = index%9
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
    def assign_cell(self, cell, value):
        self.puzzle[cell] = value
        row = cell//9
        column = cell%9
        block = self.get_box(cell)
        self.rows[row].remove(value)
        self.columns[column].remove(value)
        self.blocks[block].remove(value)

    # Loop over the puzzle repeatedly,
    # searching for cells where only a single value is possible.
    # In those cases, assign the cell to that single value.
    # For sets, the easiest is s.pop(); for list, it's... the first element!!
    def assign(self):
        while 0 in self.puzzle:
            for index,value in enumerate(self.puzzle):
                if value == 0:
                    cp = self.cell_possibilities()
                    if len(cp[index]) == 1:
                        value = cp[index][0]
                        self.assign_cell(index, value)
                else:
                    continue

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
