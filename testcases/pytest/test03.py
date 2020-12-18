import pytest

data = ['123','456']
@pytest.mark.parametrize('pwd',data)
def test1(pwd):
    print(pwd)

data2 = [(1,2,3),(4,5,6)]
@pytest.mark.parametrize('a,b,c',data2)
def test2(a,b,c):
    print(a+b+c)

def add(a,b):
    return a+b

data3 = [
    pytest.param(1,2,3,id='(a+b):pass'),
    pytest.param(4,5,9,id='(a+b):pass')
]

@pytest.mark.parametrize('a,b,expect',data3)
def test3(a,b,expect):
    assert add(a,b) == expect
