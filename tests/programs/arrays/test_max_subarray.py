# test_max_subarray.py

import pytest
from programs.arrays.max_subarray import max_subarray

def test_all_negative_array():
    output = max_subarray([-1, -2, -3, -4, -5])
    assert output == -1

def test_normal_array():
    output = max_subarray([1,3,2,5,-10,2,1])
    assert output == 11

