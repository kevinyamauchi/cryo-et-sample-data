from cryo_et_sample_data import hiv
from cryo_et_sample_data._base import DataSet


def test_hiv():
    assert hiv.name == "hiv"
    assert hiv.author == "Alister Burt"
    assert isinstance(hiv, DataSet)
