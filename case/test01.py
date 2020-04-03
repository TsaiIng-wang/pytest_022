import pytest

def test_01():
    print('执行测试用例01')

def test_02():
    print('执行测试用例02')

def test_03():
    print('执行测试用例03')

#TEST
if __name__ == '__main__':
    pytest.main(['-s','test007.py'])