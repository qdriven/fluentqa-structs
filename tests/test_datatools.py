import fluentmodels
from data_constants import more_dict, more_json_dict


def test_get_value_by_expression():
    result = fluentmodels.get_value_by_expression(more_dict,"characters.Lonestar")
    assert result == {
            "id": 55923,
            "role": "renegade",
            "items": ["space winnebago", "leather jacket"],
        }

def test_set_value_by_express():
    fluentmodels.set_value_by_expression(more_dict,"characters.Lonestar",{})
    result = fluentmodels.get_value_by_expression(more_dict,"characters.Lonestar")
    assert result == {}


def test_set_value_by_express_json():
    result = fluentmodels.set_value_by_expression(more_json_dict,"characters.Lonestar",{})
    result = fluentmodels.get_value_by_expression(result,"characters.Lonestar")
    assert result == {}


def test_differ():
    result = fluentmodels.differ(more_dict,more_json_dict)
    assert len(result)>1