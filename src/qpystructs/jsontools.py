"""
combine jmespath,jsonpath and dictor
- https://github.com/jmespath/jmespath.py
"""
import json


def loads(json_str: str, **kwargs):
    """
    load json str to json
    """
    return json.loads(json_str, **kwargs)


def load(file_path: str, **kwargs):
    """
    read json file to dict
    """
    with open(file_path) as f:
        return json.load(f, **kwargs)


def dumps(obj: dict | list, **kwargs) -> str:
    """
    dump string as json string
    """
    return json.dumps(obj=obj, **kwargs)


def get_ordered_json(obj):
    if isinstance(obj, dict):
        return sorted((k, get_ordered_json(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(get_ordered_json(x) for x in obj)
    else:
        return obj
