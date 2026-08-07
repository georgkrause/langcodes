from language_data.util import data_filename
import os

def test_data_filename():
    test = data_filename("test")
    assert str(test).endswith("language_data/data/test")
