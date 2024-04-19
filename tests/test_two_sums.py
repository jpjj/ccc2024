from source.two_sums.twosums import twoSum
import pytest

def read_two_sums(path):
    file = open(path)
    nums = list(file.readline())
    target = int(file.readline())
    res = list(file.readline())
    return nums, target, res

def test_read():
    a,b,c = read_two_sums("resource/two_sums/sums.txt")
    print("ok")

@pytest.mark.parametrize("nums, target, res", [
    ([2,7,11,13], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
    ])
def test_two_sums(nums, target, res):
    assert(twoSum(nums, target) == res)