import pytest

def test_m1():
    assert 1==2, "I is not equal to true"

def test_m2():
    assert False

def test_m3():
    assert True

def test_m4():
    msg = "success"
    assert msg == "success","String matches"