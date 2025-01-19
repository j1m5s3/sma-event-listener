from typing import Union
from enum import Enum


def select_enum_from_string(enum_type: Enum, to_convert: Union[str, list[str]]) -> Union[Enum, list[Enum]]:
    """
    Function to select an enum from a string.
    If string exists in enum, return enum, else raise error
    :param enum_type: Enum type to compare string(s) to
    :param to_convert: String or list of strings to convert to enum
    :return: Enum or list of enums
    """
    if isinstance(to_convert, str):
        for e in enum_type:
            if e.name == to_convert:
                return e
        raise ValueError(f"Invalid enum for string --> {to_convert}")
    elif isinstance(to_convert, list):
        return [select_enum_from_string(enum_type, s) for s in to_convert]




def get_strings_from_enums(enum_list: list[Enum]) -> list[str]:
    """
    Get strings from enum
    :param enum_list: List of enums to get strings from
    :return: List of enum.name
    """
    return [e.name for e in enum_list]
