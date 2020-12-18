import pytest

@pytest.mark.do
def test1():
     print('test01')

@pytest.mark.undo
def test2():
    print('test02')
