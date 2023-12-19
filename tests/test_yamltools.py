from qpystructs import jsontools
from qpystructs import yamltools


def test_to_yaml_file():
    data = jsontools.load("./example.json")
    yamltools.to_yaml_file("./example.yaml", data)
