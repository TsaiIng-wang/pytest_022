import pytest
import allure

@allure.step('步骤01')
@pytest.fixture(scope='session')
def step_01():
    print('这是步骤01')

@allure.step('步骤02')
@pytest.fixture(scope='session')
def step_02():
    print('这是步骤02')

@allure.feature('测试XX页面')
class Testxx():
    @allure.story('这是用例01')
    def test_01(self,login,step_01):
        print('执行测试用例01')
        assert 1==1

    @allure.story('这是用例02')
    def test_02(self,login,step_02):
        print('执行测试用例02')
        assert 2==2

    @allure.story('这是用例03')
    def test_03(self,login,step_01,step_02):
        print('执行测试用例03')
        assert 3==3

    def test_04(self):
        print('044')

if __name__ == '__main__':
    pytest.main(['-s','test007.py'])