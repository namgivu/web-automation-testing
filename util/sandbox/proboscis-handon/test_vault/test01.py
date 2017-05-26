"""Demo @test at method level"""

import unittest
from proboscis.asserts import assert_equal
from proboscis import test


@test(groups=["unit", "strings"])
def test_reverse():
    """Make sure our complex string reversal logic works."""
    original = "hello"
    expected = "hello"
    actual = original
    assert_equal(expected, actual)
