from source.level1.main import calc_coords, calc_smallest_rect
from source.level1.parser import parse

def test_calc_smallest_rect():
    path = "resource/level2/level2_example.in"
    N, paths = parse(path)
    res = calc_smallest_rect(N, paths)
    assert(res == [(4, 3), (3, 4), (8, 4)])
    

def test_coord():
    string = "WASD"
    res = [(0,1), (-1,1), (-1, 0), (0,0)]
    assert(res == calc_coords(string))