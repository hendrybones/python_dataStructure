import manture
import pytest


@pytest.mark.card
def test_locate_card():
    index = manture.locate_card([13, 11, 10, 7, 4, 3, 1, 0],
                                7)
    assert index == 3
