import pytest
import requests


@pytest.fixture()
def test1():
    return 11


def test_aa(test1):
    print("哈哈哈")
    print(test1)


requests