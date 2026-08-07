from language_data.util import data_filename
import os

def test_data_filename():
    test = data_filename("test")
    cwd = os.getcwd()

    assert str(test) == f"{cwd}/language_data/data/test"
