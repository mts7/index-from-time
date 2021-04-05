import pytest

from indexfromtime.main import get_index


def test_get_index_valid():
    length = 5
    index = get_index(length)
    assert index >= 0
    assert index < length


def test_get_index_wrong_type():
    with pytest.raises(TypeError):
        get_index('banana')


def test_get_index_no_value():
    with pytest.raises(TypeError):
        get_index()
