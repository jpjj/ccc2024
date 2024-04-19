from source.level1.parser import parse

def test_parse():
    path = "resource/level1/level1_example.in"
    N, paths = parse(path)
    assert(N == 3)
    assert(paths[2] == "DSASSDWDSDWWAWDDDSASSDWDSDWWAWD")