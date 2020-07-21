import os,sys
sys.path.append(os.getcwd())
from nthwithproperty309 import nthwithproperty309
import pytest


@pytest.mark.parametrize('x, result',[
	(0, 309),
	(1,418),
	(2,462),
	(3,474),
	(575),
	(635, 5),
	(662, 6),
	(2014, 100),
	(7813, 1000)
])

def test_nthwithproperty309(x, result):
    assert nthwithproperty309(x) == result
