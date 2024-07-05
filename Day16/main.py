#!/usr/bin/python

import time
import sys
output_stream = sys.stdout

FINAL_INPUT = """\\....../.-...--.|....\\../.......|......|.\\......../..................|......|......................|..........
...................|........../.........-..................................../\\|....|.........................
................/..../.........\\.....-.................................../................./...............|..
..........|.....................\\......-..-...|......-|..............|.......\\.........|...........--.......|.
.\\................................................/............../...|......|............-...................-
.......................|..................-..|...\\...|...................................|.......-......../...
...................................../.....|....|...-................-........\\....-..........................
.......--.....-.....-.-......\\..../....|........\\......../..|...................../...........................
.................-......\\......../.....-|..............|....-........-....\\......|...-.......-....../.........
...........|......-.............\\.../.........\\...........|.....-...../....................../.........|-.....
...................../........|...-.......-.............../\\\\...../..\\...........................\\............
........|.............................................................-....|.........-........-..../.....|....
....././...-.......|...../........../.|..\\.....||.............................|............\\..................
......\\...|.....|..........................-......|.....-........................................./..|.......|
..|../....|..-.-............-..../|.\\........................-../...\\............................-\\..|..-.....
.|..|....\\........\\.|.-....\\....................\\...\\......../....................../..//...|.....//..-./.....
....................|.............../...|..|.|......./..........................-..............|..|.../.......
........\\.................|/.......-...........|/....|.../.|.\\...................-...........|.............|..
.........-..|.............\\.../....|/.................|/.............\\........-..................|...|........
......../........|......\\...................|.....\\.\\.................\\......\\.........|..................\\...
.......\\...................|........./...................|.....|......./..../.|.|...-....|........../.........
...............\\.|..\\......./.....\\....../..............\\..\\...../......\\...-.........../\\...........-........
......................-.....|......../............../......|.......\\..../.............../.../.......|....../..
..............-.\\/\\.\\....................-...\\.....................\\-../.....\\..........\\...../......./.......
......./...../....\\......../........\\..|.................-...................-..........-............../......
.....|..|....|...||.|..../...\\......\\.|........\\...../......................................|..\\..............
........-....\\........./......|....../.../.......-...................................-|.......................
...................../...../.......................-........\\.........\\..|./...../.....-..........\\...........
...../........\\\\.\\\\........................-..-....................\\-.|.|-.........................\\..........
......................./...........................-.........../.........................../........-/.../....
......-........................./...\\........................\\....|.../..|../..........-................./....
..-..................-............\\........../.......\\................................................./......
.../...................|...-.../........................|-.-......./..................-.............\\.........
....\\...../............../............................-..............-../..........-.....--...................
...-.......-...\\...../...............................\\................................................|.......
............-.......................\\.-\\.....\\..............\\............-.........\\..../\\...\\...-..........\\.
\\.............|...../\\...../....../..........|./...../.......................-..................-.\\...........
.-..................-.....-..\\..........|..............\\..-......-...........//./...-..\\.......-../...........
..............|..\\..-...\\....|.........................-..|...|/.........................-./....../\\..|.....-.
...|....\\.-...................|.|..................-.....\\../..............\\............/..........-..........
........../.....|............./............................................|..-......|\\.........-........-/.|.
....|../........\\..................|...\\.........\\./....|....-.........-...\\....|............................-
-.....................|\\............/............\\...................-.|........-........../..................
-...|.../....-...../...../............\\.................|........................|.......|-...............\\-..
..\\....................../.\\..\\.....|.............-.....-....-./......-../..................\\.................
../...............|...-..\\./.....-....................../................\\............-........../.........|..
...|.........\\......\\.........-..-.|......\\...............-......-..............\\..........-\\......\\..........
..|...................\\..|.....\\.......\\...................\\............................................/.....
|..|.../.....|..../.......-..................\\......../......../.........-....................................
.....\\.......................-...\\..\\.......|........\\.............\\...|......./-\\..........|.....-.\\.........
.............................|/|.|.-............./.......|..../.........\\\\..-.|....|...../.......-..........|.
........|..../.............\\.../\\...............................................................|.............
..\\.-|......|..........................|........./........-..................-......./..........|...-.......\\.
/........|....\\....../..........||...................|.|...|....................-.|.......\\|.\\................
............./.......................-..\\\\.|.../.....|....................\\../................................
..................\\..................../...........|........\\.|........../........./........||.......-/.\\.....
........\\....-...|..|.......-...-..........................--.......\\.../..\\.................\\................
....-....\\......|..../.../......//|...........................|............./.-.|.........\\/.|..-............\\
-....\\..../....................|..\\.............\\.........-.....\\..|.-.\\.......-.........|..\\.....-...........
........../......\\...........././.....-.....|................|.............-|............./...|.......\\-......
.................-../............-..............................................-...\\.........................
\\.....|...................|.../........-..................\\.....\\/........-...................................
......\\......................./................-.........\\...-.....-.....|............./...........-..\\....\\..
......-..//....-........../.............\\....\\.\\.........\\...................\\..\\.............................
|.............-................-......................./.............................\\..-.....\\............/..
..........|..........................-.|............\\......-........\\..\\.|......|.-........................../
...................|.............-......../..-...............\\......../................/..........-\\/|..\\.....
..../|.|............................./......../.|.\\.-.................-............\\........|-..-.............
./............../.........-........|.|......|................-.|................/..............\\..............
.........-........\\..............|/............/....-..../.../.........|.........................\\............
.................../.|.\\.-....|................................|................./-........-..................
....................\\.......\\.........//..........-.../..|.....-..-................./...-.....-...............
...........|/.\\..-........./...........|.-......-...................................../...................\\...
......|....|...........\\....-..................-...............-|............-./...............|.......|.....\\
..............\\...-............/...............|..../....\\\\../................................/...........-...
../............|..../...................-........-.................|............./..\\../....\\..-....\\..\\......
.............\\...-..............|............/..........................-...................................|.
.........|...................../....-..........|........./.........|.....-......../..|..............-..../....
.....................\\...................../\\.................\\....../........./..............\\.........|.....
..................................\\./.-........................|......\\.................../...-......\\-.......
.......|.......................|............................-.........................../.....................
......\\...............-......\\...........................|........................./.-........../..../....\\...
.../....-|.......-........../..........-......\\.............|..-.../.......\\.../..../..................-......
........./.............\\....-..-...\\..--...|.-..-.|...-....-.....\\................-/.........|.............-\\.
...........|.............\\.............\\.....|....|.--............|...|.|.............................-/......
../.............|........|................./\\..|....../.............|\\............\\.........\\.......|.......|.
-...........-..................-........\\...............................-\\...................\\|......|........
..................../.......-..-...............\\..........\\..........................................\\...../|.
........|........./.......-\\.......|............|............../............../......-.....|..................
...........-..........//.....|............\\...\\................/.........-...-./..|......................-\\...
/\\........./.|..............|..........|..................-|-.........|........................-..|\\.\\.-......
............./....../..........|//.....-.....-.../....................|.......\\.......-........-...........|..
......................./..........\\............./....................\\.........-......-\\...|..................
.......................-..../../..................-.........-........................\\..............|.........
........|..../..../..-|................|.../..........|...........-................\\...............-..........
.........|.......\\.........................\\....|..............\\......\\....-............................/....-
...........\\..........|................................./....................../..............................
........................../.-....................\\........................-......|.......|.....-../...........
.............\\..-|........-.\\|....\\............./......\\.................|.........\\.-......................./
.....--...........\\.............\\../.....\\................................./....-.........|............./.../.
............................|........................\\......|/........|...................../.................
.../..|.......................................-.....|.../........................./...-.......................
.|.../../.........-....................-.................../..-......-....|................\\..................
......|.....|-....\\./.....\\.........../.............../...............\\...\\....\\......-.\\....-...\\-...-./|.../
|.|......./...-....\\....\\|\\...\\......\\..\\.......././.........\\........-.....-.........././-....-...-\\.........
.......\\.|...../.../...../.........\\..|./.................\\..-\\.........\\.....|...|.......-...............-/..
............/.-.....................\\......./..|................................../|........./.........|..-..|
.../..............././..\\.\\............|...-.|................/..-..-.........-......-.......//...............
.....\\...\\-...\\.......................-|.........|...-|...........\\.........|.....\\|...\\............-......./.
........|./......|\\.................\\....|\\.................-.../........./..............\\-.....-....../....-.""".split("\n")

TEST_INPUT = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....""".split("\n")

class Beam:
    def __init__(self, location, direction, grid):
        self.direction = direction
        self.start = location
        self.location = None
        self.grid = grid
        self.path = [location]
        self.queue = [location]
        self.energized = 0

    def travel(self):
        while(len(self.queue) > 0):
            # print(self.queue)
            self.location = self.queue.pop()
            if(self.location['energized']):
                print(self.location)
            # print(self.location['row'], self.location['col'])
            if not self.location['energized']:
                self.location['energized'] = True
                self.location['step'] = str(self.energized)
                self.energized += 1
            self.direction = self.location['direction']
            match self.direction:
                case "n": self.go_north(),
                case "e": self.go_east(),
                case "s": self.go_south(),
                case "w": self.go_west(),
            # time.sleep(.5)
            # print_grid(self.grid)

    def go_north(self):
            match self.location['symbol']:
                case '-':
                    if(self.location['col']+1 < len(self.grid[0])):
                        if not self.location['gone_east']:
                            self.grid[self.location['row']][self.location['col']+1]['direction'] = 'e'
                            self.queue.append(self.grid[self.location['row']][self.location['col']+1])
                            self.location['gone_east'] = True
                    if(self.location['col']-1 >= 0):
                        if not self.location['gone_west']:
                            self.grid[self.location['row']][self.location['col']-1]['direction'] = 'w'
                            self.queue.append(self.grid[self.location['row']][self.location['col']-1])
                            self.location['gone_west'] = True
                case '\\':
                    if not self.location['gone_west']:
                        if(self.location['col']-1 < len(self.grid[0])):
                            self.grid[self.location['row']][self.location['col']-1]['direction'] = 'w'
                            self.queue.append(self.grid[self.location['row']][self.location['col']-1])
                            self.location['gone_west'] = True
                case '/':
                    if not self.location['gone_east']:
                        if(self.location['col']+1 < len(self.grid[0])):
                            self.grid[self.location['row']][self.location['col']+1]['direction'] = 'e'
                            self.queue.append(self.grid[self.location['row']][self.location['col']+1])
                            self.location['gone_east'] = True
                case _:
                    if not self.location['gone_north']:
                        if(self.location['row']-1 >= 0):
                            self.grid[self.location['row']-1][self.location['col']]['direction'] = 'n'
                            self.queue.append(self.grid[self.location['row']-1][self.location['col']])
                            self.location['gone_north'] = True

    def go_east(self):
            match self.location['symbol']:
                case '|':
                    if(self.location['row']+1 < len(self.grid)):
                        if not self.location['gone_south']:
                            self.grid[self.location['row']+1][self.location['col']]['direction'] = 's'
                            self.queue.append(self.grid[self.location['row']+1][self.location['col']])
                            self.location['gone_south'] = True
                    if(self.location['row']-1 >= 0):
                        if not self.location['gone_north']:
                            self.grid[self.location['row']-1][self.location['col']]['direction'] = 'n'
                            self.queue.append(self.grid[self.location['row']-1][self.location['col']])
                            self.location['gone_north'] = True
                case '\\':
                    if not self.location['gone_south']:
                        if(self.location['row']+1 < len(self.grid)):
                            self.grid[self.location['row']+1][self.location['col']]['direction'] = 's'
                            self.queue.append(self.grid[self.location['row']+1][self.location['col']])
                            self.location['gone_south'] = True
                case '/':
                    if not self.location['gone_north']:
                        if(self.location['row']-1 >= 0):
                            self.grid[self.location['row']-1][self.location['col']]['direction'] = 'n'
                            self.queue.append(self.grid[self.location['row']-1][self.location['col']])
                            self.location['gone_north'] = True
                case _:
                    if not self.location['gone_east']:
                        if(self.location['col']+1 < len(self.grid[0])):
                            self.grid[self.location['row']][self.location['col']+1]['direction'] = 'e'
                            self.queue.append(self.grid[self.location['row']][self.location['col']+1])
                            self.location['gone_east'] = True

    def go_south(self):
            match self.location['symbol']:
                case '-':
                    if(self.location['col']+1 < len(self.grid[0])):
                        if not self.location['gone_east']:
                            self.grid[self.location['row']][self.location['col']+1]['direction'] = 'e'
                            self.queue.append(self.grid[self.location['row']][self.location['col']+1])
                            self.location['gone_east'] = True
                    if(self.location['col']-1 >= 0):
                        if not self.location['gone_west']:
                            self.grid[self.location['row']][self.location['col']-1]['direction'] = 'w'
                            self.queue.append(self.grid[self.location['row']][self.location['col']-1])
                            self.location['gone_west'] = True
                case '\\':
                    if not self.location['gone_east']:
                        if(self.location['col']+1 < len(self.grid[0])):
                            self.grid[self.location['row']][self.location['col']+1]['direction'] = 'e'
                            self.queue.append(self.grid[self.location['row']][self.location['col']+1])
                            self.location['gone_east'] = True
                case '/':
                    if not self.location['gone_west']:
                        if(self.location['col']-1 >= 0):
                            self.grid[self.location['row']][self.location['col']-1]['direction'] = 'w'
                            self.queue.append(self.grid[self.location['row']][self.location['col']-1])
                            self.location['gone_west'] = True
                case _:
                    if not self.location['gone_south']:
                        if(self.location['row']+1 < len(self.grid)):
                            self.grid[self.location['row']+1][self.location['col']]['direction'] = 's'
                            self.queue.append(self.grid[self.location['row']+1][self.location['col']])
                            self.location['gone_south'] = True

    def go_west(self):
            match self.location['symbol']:
                case '|':
                    if(self.location['row']+1 < len(self.grid)):
                        if not self.location['gone_south']:
                            self.grid[self.location['row']+1][self.location['col']]['direction'] = 's'
                            self.queue.append(self.grid[self.location['row']+1][self.location['col']])
                            self.location['gone_south'] = True
                    if(self.location['row']-1 >= 0):
                        if not self.location['gone_north']:
                            self.grid[self.location['row']-1][self.location['col']]['direction'] = 'n'
                            self.queue.append(self.grid[self.location['row']-1][self.location['col']])
                            self.location['gone_north'] = True
                case '\\':
                    if not self.location['gone_north']:
                        if(self.location['row']-1 < len(self.grid)):
                            self.grid[self.location['row']-1][self.location['col']]['direction'] = 'n'
                            self.queue.append(self.grid[self.location['row']-1][self.location['col']])
                            self.location['gone_north'] = True
                case '/':
                    if not self.location['gone_south']:
                        if(self.location['row']+1 < len(self.grid)):
                            self.grid[self.location['row']+1][self.location['col']]['direction'] = 's'
                            self.queue.append(self.grid[self.location['row']+1][self.location['col']])
                            self.location['gone_south'] = True
                case _:
                    if not self.location['gone_west']:
                        if(self.location['col']-1 >= 0):
                            self.grid[self.location['row']][self.location['col']-1]['direction'] = 'w'
                            self.queue.append(self.grid[self.location['row']][self.location['col']-1])
                            self.location['gone_west'] = True

def generate_cells(grid):
    new_grid = []
    for row in range(len(grid)):
        new_grid.append([])
        for col in range(len(grid[0])):
            new_grid[row].append({"symbol": grid[row][col], "energized": False, "step": 0, "row": row, "col": col, "direction": None, "gone_east": False, "gone_north": False, "gone_south": False, "gone_west": False})
    return new_grid

def print_grid(grid):
    for row in range(len(grid)):
        row_str = ''
        for col in range(len(grid[0])):
            if grid[row][col]['symbol'] in "|-\\/" and grid[row][col]['energized']:
                row_str += grid[row][col]['symbol']
            elif grid[row][col]['energized']:
                # row_str += grid[row][col]["direction"]
                if(grid[row][col]['direction'] == 'e'):
                    row_str += '>'
                elif(grid[row][col]['direction'] == 'w'):
                    row_str += '<'
                elif(grid[row][col]['direction'] == 's'):
                    row_str += 'V'
                else:
                    row_str += '^'
            else:
                row_str += '.'
        print(row_str)
    print()

if __name__ == "__main__":
    grid = generate_cells(FINAL_INPUT)
    grid[0][0]['direction'] = "e"
    b = Beam(grid[0][0], 'e', grid)
    b.travel()
    print_grid(b.grid)
    print(b.energized)
