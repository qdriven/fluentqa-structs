#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
covert yaml to object or object to yaml string or file
"""
from typing import Any
from typing import Dict
from typing import Type
from typing import TypeVar
from typing import Union

import yaml

from pydantic_yaml import parse_yaml_file_as
from pydantic_yaml import to_yaml_str

from qpystructs import GenericDataModel


T = TypeVar("T", bound=GenericDataModel)


class YamlGenericModel(GenericDataModel):
    def to_yaml_file(self, file_path: str):
        to_yaml_file(file_path, self.model_dump(by_alias=True))


def load_yaml(model_type: Type[T], file_path: str) -> Any:
    return parse_yaml_file_as(model_type, file_path)


def to_yaml_file(file_path: str, data: Union[YamlGenericModel, Dict]):
    if isinstance(data, YamlGenericModel):
        yaml_str = to_yaml_str(data)
    else:
        yaml_str = yaml.dump(data)
    with open(file_path, "w") as f:
        f.write(yaml_str)
