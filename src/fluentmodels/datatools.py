from typing import Dict, Any, Union
import jmespath
from pydantic.main import BaseModel

from fluentmodels.jsontools import loads
from dotty_dict import dotty


def get_value_by_expression(target_object: Any, path_exp: str) -> Any | None:
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


def set_value_by_expression(json_dict: Union[str, Dict], path_exp: str, to_value: Any) -> Dict:
    dot = dotty(json_dict)
    dot[path_exp] = to_value
    return dot.to_dict()


from deepdiff import DeepDiff


def differ(expected_data: Union[str, dict], actual_data: Union[str, dict]):
    if isinstance(expected_data, str):
        v1 = loads(expected_data)
        v2 = loads(actual_data)
    else:
        v1 = expected_data
        v2 = actual_data

    return DeepDiff(v1, v2, verbose_level=2)
