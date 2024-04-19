from typing import List


def parse(path):
    file = open(path)
    N = int(file.readline())
    paths = []
    for i in range(N):
        paths.append(file.readline()[:-1])
    return N, paths

def write(name, res: List[List[int]]):
    f = open(name, "a")
    for lin in res:
        f.write(" ".join([str(x) for x in lin]) + "\n")
    f.close()

write("hallo.txt", [[1,2,3], [2,3,4]])