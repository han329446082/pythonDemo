import pytest

@pytest.fixture()
def init():
    print('int...')
    return 1

def test1(init):
    print('test1...')

def test2(init):
    print('test2...')

def test3():
    print('test3...')

if __name__ == '__main__':
    pytest.main(['-vs','test04.py'])
