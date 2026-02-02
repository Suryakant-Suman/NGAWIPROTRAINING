import pytest
import sys

@pytest.mark.skip(reason="Feature under development")
def test_skip_example():
    assert False

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_conditional_skip():
    assert True

@pytest.mark.xfail(reason="Known bug")
def test_xfail_example():
    assert 1 / 0 == 0
