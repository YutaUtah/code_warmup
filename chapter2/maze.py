from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, node_to_path, bfs, astar

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows=10, columns=10, sparseness=0.2, start=MazeLocation(0,0), goal=MazeLocation(9,9)):
        # create the basic instance variable
        self._rows = rows
        self._columns = columns
        self.start = start
        self.goal = goal

        # create empty cell
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        # obstacles
        self._randomly_fill(rows, columns, sparseness)

        # start/goal
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0,1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED


    def __str__(self):
        output = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output


maze = Maze()
print(maze)




