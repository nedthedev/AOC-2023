#!/usr/bin/python

TEST_INPUT = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

def find_hz_mirror(map):
    first_match = None
    for top_row in range(len(map)//2):
        for bot_row in range(len(map)//2):
            if(first_match):
                top_row = bot_row
            print(f"Comparing {map[top_row]} to {map[bot_row]}")
            if(map[top_row] == map[-bot_row]):
                if(first_match is None):
                    first_match = (top_row, bot_row)
            else:
                if(first_match is not None):
                    return False
    return first_match


if __name__ == "__main__":
    maps = TEST_INPUT.split("\n\n")
    for map in maps:
        print(find_hz_mirror(map.split("\n")))