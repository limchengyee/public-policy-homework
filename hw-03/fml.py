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
                row = index//9
                column = index%9
                if row <= 2 and column <= 2:
                    block = 0
                if 2 < row <=5 and column <=2:
                    block = 1
                if 5 < row <=8 and column <=2:
                    block = 2
                if row <= 2 and 2 < column <= 5:
                    block = 3
                if 2 < row <=5 and 2 < column <= 5:
                    block = 4
                if 5 < row <=8 and 2 < column <= 5:
                    block = 5
                if row <=2 and 5 < column <= 8:
                    block = 6
                if 2 < row <=5 and 5 < column <= 8:
                    block = 7
                if 5 < row <=8 and 5 < column <= 8:
                    block = 8
                self.blocks[block].remove(value)

    def __repr__(self):

         return "".join(str(x) for x in self.puzzle) + "\n"

    def get_box(self, cell):
        return 0

      # Get the possibilities for the row, column, and box.
      # Their intersection is the possibilities of the cell.
    def cell_possibilities(self):
            x = []
            for i in range(81):
                x.append([])
                row = i% 9
                column = i%9
                block = int(row/3)*3 + int(column/3)
                for j in self.rows[row]:
                    if j in self.columns[column] and j in self.blocks[block]:
                        x[i].append(j)
            return x


    # Assign a cell to a value,
    # and remove the possibilities from the row, column, and box.
    def assign_cell(self, cell, value):
        while 0 in self.puzzle:
            for index,value in enumerate(puzzle):
                if value == 0:
                    continue
                cp = self.cell_possibilities()
                if len(cp) == 1:
                    value = cp.pop()
                    self.rows[row].remove(value)
                    self.columns[column].remove(value)
                    self.blocks[block].remove(value)
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
#    break

#    total += 1
#    if s.verify_solution(): solved += 1

    out.write(s.__repr__())

print("Easy {}/{} = {:.3f}".format(solved, total, solved/total))

#line = '''001700509573024106800501002700295018009400305652800007465080071000159004908007053'''
'''bulba = sudoku(line)
y = bulba.cell_possibilities()
print(y)
'''
