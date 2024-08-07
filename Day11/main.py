#!/usr/bin/python

import time

def final_input():
    return """....................#........#...............................#............................................................#................#
............#...................................#........................................#........#..................#...........#..........
.#.......................#..................................................................................................................
..........................................................#.................................................#...............................
...................................#..........................................#.............................................................
...........................................#......................#.........................................................................
......................#.....................................................................................................................
..................................................#.........#.........#.......................#............................#.......#......#.
......#.........#............#.............................................#................................................................
.#................................#.....................#.......................#........................#..................................
..........................................#.................................................................................................
.......................................................................................#......................#.............................
.....................................................................#..............................................#.....#.................
........#.................#.................................................................................................................
....................................#.................#........................................................................#............
.............#...........................#.......................#................#..................#.................................#....
#...........................................................................#...............................................................
......................#......#..............................................................................................................
.................................................#........................................................#.................................
.....................................#...................................................#........................#.........................
........#................#................................#.................................................................................
...................#................................................................#........#...............#..............#...............
.......................................................................................................#..........................#.........
..................................#.......#.........................................................................#...................#...
.............#.................................#........................#...................................................................
.....................#..................................#......................................#................#...........................
...............................................................#.....................#..................................#...................
#.........#...................#................................................#........................#...................................
...................................#..................................#............................................................#........
............................................#.........#...........................................#.........................................
...#.............................................#........................................................................#.................
........#..........#........#.................................................................................#.................#......#....
..............................................................#..................#..........................................................
.....................................................................#......................................................................
.................................................................................................................#..........................
...............#...............................#....................................................#.......................................
...........................#................................................................#........................................#......
...........#.....................#..................#............#...........#.......#.....................#................................
............................................................................................................................................
...............................................................................................................................#.........#..
.......................................................................................................................#....................
........#................#.....#.....#.................#.........................................#..........................................
..................................................#...................................#.....................................................
....#...........#.............................................................#..............#...............#...................#..........
............................................#...............#.........................................................................#.....
....................#.......................................................................................................................
#......#..........................#..................#...............#.....#................................................................
...........................................................................................#......................#........................#
...........#................................................................................................................................
...............................................................................#...................#........................................
.......................#..............#......#..............#...........................#..................................#................
............................................................................................................................................
...................#...........#.................................................................................................#..........
.......................................................................................................#.....#..............................
........................................................#...........................#................................#......................
...............#...................................................#..........#...........#.................................................
...........................................#......................................................#.........................................
.........#.......................................#..........................................................................................
..........................#...............................................................................#........#......................#.
...........................................................#...............#...........#......#..........................#..................
.................#......................#.............................#........................................................#............
.............................................................................................................#..............................
...............................#...............................................#............................................................
............................................#.........#.....................................................................#...............
...#......................#........#.............................................................#..................#.....................#.
................................................#..............#.......................#..............#.....................................
............................................................................................................................................
#...........................................................................................................................................
......#..............#....................................#........#................................................................#.......
..............#.............#.........#..........................................#..........................................................
..................................................................................................#............................#..........#.
...........................................#...................#.......................................#.....#..............................
.................................#....................#................................#....................................................
............................................................................................................................................
........................................................................#...................................................#...............
..#..............................................#...........................................#...................#.....#.............#......
......................#.....................................................................................................................
...............................#......#..........................................................#.......#.....................#............
..........#.....#.................................................#.............#...........................................................
............................................................................................................................................
............................#.................................#.........#...................................................................
.......................................................#................................#...........................#.......................
...........................................................................................................................#.........#......
...................#..............................#..............................#...............#.........#................................
..........#..............#.....................................................................................................#............
............................................................................................................................................
................#.........................................................#...............................................................#.
.................................#.....................................................................#....................................
.....#................................................#.....................................#...............................................
.............................#...............................#................#..............................#..............................
......................................................................................#...............................#........#............
............................................................................................................................................
...........#..........#..............................................#..............................................................#.......
................................................#..............#...................................................#........................
......#...........#.........................................................#...............#...............................................
...............................#.....................................................#...............#...................................#..
..............#.......................#.....................#...............................................................................
.........................#........................#...........................................................................#......#......
.........................................................................................................#..................................
............................................................................................................................................
...#......................................................#.................................................................................
........................................#.................................................#........#..............#.....#...................
....................#................................#..........................#...........................................................
#.................................#..................................................#.........#.......#.............................#......
...........#.........................................................#.......................................................#..............
......#......................#.................#.............................#..............................................................
........................................................#.........................................#............#.................#..........
..................#....................#.....................................................#..............................................
..........................#......................................................#......#................................#..................
................................#............#.........................................................#.................................#..
............................................................................................................................................
...#........................................................#...............................................................................
..............#.....................................#................................................................................#......
....................................................................................................................#...........#...........
...................#.........................................................................#..............................................
.............................#........#.....................................................................................................
................................................................#................................................#..........................
..#..........#...................................#..............................#........#................#.................................
..................................#........................................................................................#................
.....................#....................................#....................................#.....#......................................
........#.......#..............................................................................................#...................#........
...........................#..............#..........#............#......................................................................#..
.#..........................................................................................................................................
............#....................................#.....................................................................#....................
.............................................................#.............#.........#.....#........#.......................................
......#...........................#.......................................................................#.................................
........................................................#..................................................................#................
#..........................#.............#.........................#..........#...................................#.........................
....................#....................................................................#.............#..........................#.....#...
............................................................................................................................................
.....................................................#..................#................................................#..................
...#....................#......#............................#.....................#.................#.......................................
............#...................................#...........................................................................................
............................................................................................#...............................................
...................#...................................................................#..................#.................#.........#.....
#.................................#........#..........#..........................................#..........................................
.....#......................................................................................................................................
.......................#................................................#........................................#..........................
.................................................................#...........#............#..........#...................................#..
..............#......................#.......#.........................................................................#....................""".split("\n")

def test_input():
    return """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......""".split("\n")

class Grid:
    def __init__(self, data):
        self.grid = self.grid_to_cells(data)
        self.grid = self.expand_space()
        self.link_cell_neighbors()
        self.galaxies = self.find_galaxies()

    def expand_space(self):
        for row in self.grid:
            empty = True
            for cell in row:
                if cell.symbol == "#":
                    empty = False
            if(empty):
                for cell in row:
                    cell.cost *= 2
        columns_to_dup = []
        for col in range(len(self.grid[0])):
            empty = True
            for row in range(len(self.grid)):
                if(self.grid[row][col].symbol == "#"):
                    empty = False
            if(empty):
                columns_to_dup.append(col)
        for col in columns_to_dup:
            print(col)
            for row_num in range(len(self.grid)):
                self.grid[row_num][col].cost *= 2
        return self.grid
    
    def print(self, grid=None):
        if(not grid):
            grid = self.grid
        for y, row in enumerate(grid):
            string = ""
            for x in range(len(row)):
                # if(self.grid[y][x].symbol == "#"):
                # if(self.grid[y][x].on_path):
                #     string += "X"
                # else:
                #     string += "."
                # else:
                string += str(grid[y][x].cost)
                # string += "\t"
            print(string)
        print()

    def grid_to_cells(self, grid):
        cell_grid = []
        for y, row in enumerate(grid):
            cell_grid.append([])
            for x in range(len(row)):
                cell_grid[y].append(Node((x, y), grid[y][x]))
        return cell_grid
    
    def reset(self):
        for row, cells in enumerate(self.grid):
            for col in range(len(cells)):   
                self.grid[row][col].reset()

    def mark_path(self, start, dest):
        dest.on_path = True
        next = dest.parent
        while(next != start):
            next.print()
            next.on_path = True
            next = next.parent
        return

    def link_cell_neighbors(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                north = east = south = west = None
                if(row-1 >= 0): north = self.grid[row-1][col]
                if(col+1 < len(self.grid)): east = self.grid[row][col+1]
                if(row+1 < len(self.grid)): south = self.grid[row+1][col]
                if(col-1 >= 0): west = self.grid[row][col-1]
                self.grid[row][col].neighbors = (north, east, south, west)

    def find_galaxies(self):
        galaxies = []
        for y, row in enumerate(self.grid):
            for x in range(len(row)):
                if(self.grid[y][x].symbol == "#"):
                    # self.grid[y][x] = Galaxy(self.grid[y][x])
                    # self.grid[y][x].symbol = str(len(galaxies)+1)
                    galaxies.append(self.grid[y][x])
        return galaxies

class Node:
    def __init__(self, coord, symbol, cost=1):
        self.coord = coord
        self.symbol = symbol
        self.cost = cost
        self.weight = 1
        self.parent = None
        self.on_path = False
        self.traversed = False
        self.distance_map = []
        self.neighbors = []

    def calculate_distances(self, grid):
        # self.grid = grid.grid.copy() # create a copy of the star map
        # self.grid = grid
        tmp_grid = grid.grid.copy()

        stack = [self] # stack to act as queue
        while(len(stack) > 0):
            for node in stack[0].neighbors:
                if(node and stack[0].weight+node.cost < node.weight):
                    node = tmp_grid[node.coord[1]][node.coord[0]]
                    node.weight = stack[0].weight+node.cost
                    node.parent = stack[0]
                    stack.append(node)
            stack = stack[1:]
        return tmp_grid

    def get_distance(self, dest):
        # start.weight = start.cost
        # start.on_path = True
        # start.direction = 'e'
        # queue = [start]
        # directions = ['n', 'e', 's', 'w']
        # while(len(queue) > 0):
        #     cell = queue.pop()
        #     for index, neighbor in enumerate(cell.neighbors):
        #         if(neighbor):
        #             total_cost = cell.weight + neighbor.cost
        #             if(check_chain(cell) and total_cost < neighbor.weight):
        #                 neighbor.weight = total_cost
        #                 neighbor.direction = directions[index]
        #                 cell.direction = neighbor.direction
        #                 queue.append(neighbor)
        #                 neighbor.parent = cell
        #                 cell.child = neighbor
        #             cell.explored = True
        return (abs(self.coord[1] - dest.coord[1]) + abs(self.coord[0] - dest.coord[0]))

    def reset(self):
        # self.weight = 1
        self.on_path = False

    def print(self):
        print(f"Location: {self.coord}\tSymbol: {self.symbol}\tNeighbors: {self.neighbors}\tCost: {self.cost}")

# class Galaxy(Node):

#     def __init__(self, node):
#         super().__init__(node.coord, node.symbol, node.weight)
#         self.neighbors = node.neighbors
#         self.grid = []

#     def calculate_distances(self, grid):
#         # self.grid = grid.grid.copy() # create a copy of the star map
#         # self.grid = grid

#         stack = [self] # stack to act as queue
#         while(len(stack) > 0):
#             for node in stack[0].neighbors:
#                 if(node and stack[0].weight+1 < node.weight):
#                     node.weight = stack[0].weight+1
#                     stack.append(node)
#             stack = stack[1:]
#             grid.print()
#             time.sleep(.1)

if __name__ == "__main__":
    g = Grid(test_input())

    sum = 0
    pairs = 0
    for index, galaxy in enumerate(g.galaxies):
        galaxy.weight = 0
        # galaxy.calculate_distances(g)
        galaxy_sum = 0
        for destination in g.galaxies[index+1:]:
            pairs+=1
            # print(f"Distance from {galaxy.coord} to {destination.coord} is {destination.weight}")
            # galaxy_sum += destination.weight
            galaxy_sum += galaxy.get_distance(destination)
            # g.mark_path(galaxy, destination)
            # g.print()
        # print(galaxy_sum)
        sum += galaxy_sum
        g.print()
        g.reset()
    print(pairs)
    print(sum)
