# -*- coding: utf-8 -*-

from .context import landowner

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()