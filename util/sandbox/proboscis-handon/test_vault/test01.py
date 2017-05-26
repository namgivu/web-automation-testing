"""Demo @test at method level"""

from proboscis.asserts import assert_equal
from proboscis import test


@test(groups=["unit", "string"])
def test_reverse():
    """Make sure our complex string reversal logic works."""
    original = "hello"
    expected = "hello"
    actual = original
    assert_equal(expected, actual)
