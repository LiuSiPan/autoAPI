import pytest


@pytest.fixture(scope="class")
def aaa():
    print("哈哈哈哈哈哈哈哈哈")
    return 99

@pytest.fixture()
class test1():
    def test_aaa(self,aaa):
        print(aaa)

    def test_bb(self,aaa):
        print(aaa)

class test2():
    def test_aaa(self,aaa):
        print(aaa)

    def test_bb(self,aaa):
        print(aaa)

tt = test1()
tt.test_aaa()
# tt.test_bb()