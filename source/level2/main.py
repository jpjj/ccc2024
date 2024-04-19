
from source.level1.main import get_rect
from source.level1.parser import parse, write

for i in [1,2,3,4,5]:
    N, paths = parse(f"resource/level2/level2_{i}.in")
    res = get_rect(N, paths)
    write(f"resource/level2/level2_{i}.out", res)