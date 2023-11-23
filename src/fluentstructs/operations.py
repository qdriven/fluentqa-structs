import copy
import json
from typing import Dict, Any, Union, List
import jmespath
from pydantic.main import BaseModel

from .models import BaseDataModel
from .jsontools import loads
from dotty_dict import dotty

__all__ = [
    "get_value", "set_value", "differ"
]


def get_value(target_object: Any, path_exp: str) -> Any | None:
    """
    get value json/dict/class object
    """
    if isinstance(target_object, Dict):
        return jmespath.search(expression=path_exp, data=target_object)
    if isinstance(target_object, str):
        return jmespath.search(data=loads(target_object), expression=path_exp)
    if isinstance(target_object, BaseModel):
        return jmespath.search(data=target_object.dict(), expression=path_exp)
    raise NotImplementedError("not support type " + type(target_object))


def set_value(json_dict: Union[str, Dict], path_exp: str, to_value: Any) -> Dict:
    """
    set new value in a dict, return a new dict with new value
    """
    dict_value = copy.deepcopy(json_dict)
    if isinstance(json_dict, str):
        dict_value = json.loads(dict_value)
    dot = dotty(dict_value)
    dot[path_exp] = to_value
    return dot.to_dict()


from deepdiff import DeepDiff


class DifferModel(BaseDataModel):
    category: str
    difference: dict | Any


def _extract_diff(difference: DeepDiff) -> List[DifferModel]:
    result = []
    for key, value in difference.items():
        result.append(DifferModel(category=key, difference=value))
    return result


def differ(expected_data: Union[str, dict], actual_data: Union[str, dict]):
    if isinstance(expected_data, str):
        v1 = loads(expected_data)
    else:
        v1 = expected_data
    if isinstance(actual_data, str):
        v2 = loads(actual_data)
    else:
        v2 = actual_data
    return _extract_diff(DeepDiff(v1, v2, verbose_level=2))
