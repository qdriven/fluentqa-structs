import fluentstructs
from data_constants import more_dict, more_json_dict


def test_get_value_by_expression():
    result = fluentstructs.get_value(more_dict, "characters.Lonestar")
    assert result == {
        "id": 55923,
        "role": "renegade",
        "items": ["space winnebago", "leather jacket"],
    }


def test_set_value_by_express():
    new_dict = fluentstructs.set_value(more_dict, "characters.Lonestar", {})
    result = fluentstructs.get_value(new_dict, "characters.Lonestar")
    assert result == {}


def test_set_value_by_express_json():
    result = fluentstructs.set_value(more_json_dict, "characters.Lonestar", {})
    result = fluentstructs.get_value(result, "characters.Lonestar")
    assert result == {}


def test_differ():
    result = fluentstructs.differ(more_dict, more_json_dict)
    assert len(result) > 1
