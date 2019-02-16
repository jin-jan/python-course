"""
python3 -m pytest
"""
import pytest
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0,parent_dir)
from hwk6 import advanced_loops

@pytest.mark.parametrize("input_rows,input_cols",
    [("@##!",3),
     (3,"#$%"),
     (-3,3),
     (3,-1),
     (True, 3),
     (3, True),
     (7,2),
     ([1,2,3],3),
     (4,[1,2,3]),
     (1, 1000),
     (100000, 1),
     (3.4, 3),
     (3, 3.4),
     (0x10, 3),
     (3,0b10),
     (2+3j,4),
     (4,2+3j)])
def test_error_handling(input_rows,input_cols):
    """
    Test to validate hwk6 play_board function
    """
    assert not  advanced_loops.play_board(input_rows, input_cols) 
