from enum import Enum

from pydantic import BaseModel
from pydantic import field_validator
from pydantic import validator
from pydantic_yaml import parse_yaml_raw_as
from pydantic_yaml import to_yaml_str


class MyEnum(str, Enum):
    """A custom enumeration that is YAML-safe."""

    a = "a"
    b = "b"


class InnerModel(BaseModel):
    """A normal pydantic model that can be used as an inner class."""

    fld: float = 1.0


class MyModel(BaseModel):
    """Our custom Pydantic model."""

    x: int = 1
    e: MyEnum = MyEnum.a
    m: InnerModel = InnerModel()

    @field_validator("x")
    def _chk_x(cls, v: int) -> int:  # noqa
        """You can add your normal pydantic validators, like this one."""
        assert v > 0
        return v


def test_ModelJsonYaml():
    ## Model
    m1 = MyModel(x=2, e="b", m=InnerModel(fld=1.5))

    # This dumps to YAML and JSON respectively
    yml = to_yaml_str(m1)
    jsn = m1.model_dump_json()

    # This parses YAML as the MyModel type
    m2 = parse_yaml_raw_as(MyModel, yml)
    assert m1 == m2

    # JSON is also valid YAML
    m3 = parse_yaml_raw_as(MyModel, jsn)
    assert m1 == m3
