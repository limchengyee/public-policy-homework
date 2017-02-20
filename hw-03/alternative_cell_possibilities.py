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

    def cell_possibilities(self):
        self.cell_possibilities = [[x for x in range(1,10)] for i in range(9)]
        for index,value in enumerate(self.puzzle):
            if value != 0:
                row = index//9
                self.cell_possibilities[row].remove(value)

                column = index%9
                self.cell_possibilities[column].remove(value)

                block = int(row/3)*3 + int(column/3)
                self.cell_possibilities[block].remove(value)
            print(self.cell_possibilities)
            return

line = '''001700509573024106800501002700295018009400305652800007465080071000159004908007053'''
bulba = sudoku(line)
y = bulba.cell_possibilities()
print(y)
