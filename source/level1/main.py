from typing import List

from parser import parse, write


def count_directions(N: int, paths: List[str]):
    result = []
    for string in paths:
        num_W = 0
        num_A = 0
        num_S = 0
        num_D = 0
        for char in string:
            if char  == "W":
                num_W += 1
            elif char == "A":
                num_A += 1
            elif char == "S":
                num_S += 1
            elif char == "D":
                num_D += 1
        result.append([num_W, num_D, num_S, num_A])
    return result


def calc_coords(path: str):
    x = 0
    y = 0
    coords = [(x,y)]
    for char in path:
        if char  == "W":
            y += 1
        elif char == "A":
            x -= 1
        elif char == "S":
            y -= 1
        elif char == "D":
            x += 1
        coords.append((x,y))
    return coords

def calc_smallest_rect(coords):
    min_x = min([a for (a,_) in coords])
    min_y = min([b for (_,b) in coords])
    max_x = max([a for (a,_) in coords])
    max_y = max([b for (_,b) in coords])

    return (max_x - min_x + 1, max_y - min_y + 1)


def get_rect(N, paths: List[str]):
    result = []
    for path in paths:
        smallest_rect = calc_smallest_rect(calc_coords(path))
        result.append(smallest_rect)
    return result


def check_valid_path(lawn_dims, tree_coords, path):
    coords = calc_coords(path)
    smallest_rect = calc_smallest_rect(coords)


# for i in [1,2,3,4,5]:
#     N, paths = parse(f"resource/level1/level1_{i}.in")
#     res = count_directions(N, paths)
#     write(f"resource/level1/level1_{i}.out", res)

for i in [1,2,3,4,5]:
    N, paths = parse(f"resource/level2/level2_{i}.in")
    res = get_rect(N, paths)
    write(f"resource/level2/level2_{i}.out", res)