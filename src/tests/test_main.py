from nose.tools import assert_equal, assert_almost_equal, assert_greater
from src.main import _calculate_p_value, runs
import numpy as np

"""
High level testing of the package.
"""


class TestMain(object):
    def test_calculate_p_value(self):
        p_val34 = _calculate_p_value(-3.4)
        assert_almost_equal(.0003, p_val34, delta=0.0001)
        p_val09 = _calculate_p_value(-0.9)
        assert_almost_equal(.1841, p_val09, delta=0.0001)
        p_val1 = _calculate_p_value(1)
        assert_almost_equal(.8413, p_val1, delta=0.0001)

    def test_runs(self):
        list_dist_A = np.random.chisquare(2, 100)
        list_dist_B = np.random.chisquare(1, 100)
        p_val = runs(list_dist_A, list_dist_B)
        assert_greater(p_val, 0.05)

        list_dist_A = np.random.exponential(2, 100)
        list_dist_B = np.random.exponential(1, 100)
        p_val = runs(list_dist_A, list_dist_B)
        assert_greater(p_val, 0.05)
