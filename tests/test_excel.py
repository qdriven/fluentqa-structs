"""Tests for hello function."""
from typing import Optional

from pydantic import Field

from qpystructs import BaseDataModel
from qpystructs import exceltools
from qpystructs.exceltools import read_csv_to_objects
from qpystructs.exceltools import read_excel_to_objects
from qpystructs.exceltools import write_objects_to_csv


class UnitExcelModel(BaseDataModel):
    unit_group_name: str = Field("", alias="单位组名称")
    unit_name: str = Field("", alias="单位名")
    unit_symbol: Optional[str] = Field("", alias="单位符号")
    unit_latex: Optional[str] = Field("", alias="单位符号LaTex")
    base_unit: Optional[bool] = Field("", alias="基准单位")
    factor: Optional[str] = Field("", alias="换算系数")


def test_load_objects_from_excel():
    result = read_excel_to_objects("./unit_demo.xlsx", UnitExcelModel)
    print(result)
    print(type(result))

    write_objects_to_csv("unit.csv", result)
    read_csv_to_objects("unit.csv", UnitExcelModel)


def test_write_excels():
    u = UnitExcelModel()
    u.unit_name = "质量"
    u.unit_group_name = "kg"
    u1 = UnitExcelModel(unit_name="test1", unit_group_name="group1")
    list_objects = [u, u1]
    exceltools.write_objects_to_excel(list_objects, "unit_demo.xlsx")
    exceltools.write_objects_to_excel(list_objects, "unit_demo.csv")
