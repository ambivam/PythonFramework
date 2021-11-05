import pytest

@pytest.mark.smoke
def test_m3():
    assert True

def test_m4():
    msg = "success"
    assert msg == "success","String matches"


def test_m5():
    assert True

@pytest.mark.smoke
def test_m6():
    msg = "success"
    assert msg == "success","String matches"