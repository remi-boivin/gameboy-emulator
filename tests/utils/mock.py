#!/usr/local/bin python3.10
# coding: utf-8
# File: __init__.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from typing import Dict, List, Type, TypeVar, Union, Optional
from unittest.mock import MagicMock

# Todo: Add support for multiple datas


def mock_fn(data, fn=None):
    """
    Returns a MagicMock object with side_effect set to the given data.

    Args:
    - data: the data to be set as the side effect of the MagicMock object.
    - fn (optional): the MagicMock object to be returned. If not given, a new MagicMock object will be created.

    Returns:
    - A MagicMock object with the side_effect set to the given data.
    """
    if fn is None:
        fn = MagicMock()
    fn.side_effect = data
    return fn


T = TypeVar('T')


def build_dataclass(cls: Type[T], x: Dict[str, Union[str, int, List, Dict]], key: Optional[str] = None, nested_data_class: Optional[Type[T]] = None) -> T:
    """
    Builds a dataclass instance from a dictionary with optional nested dataclass instances.

    Args:
    - cls: the type of the dataclass to build.
    - x: the dictionary containing the data to build the instance.
    - key: the key in x containing the nested dataclass instance(s).
    - nested_data_class: the type of the nested dataclass to build.

    Returns:
    - A new instance of the given dataclass type, with the values from the given dictionary and the optional nested dataclass instance(s).

    If `key` and `nested_data_class` are specified, this function also supports nested dataclasses.
    If `key` is not None, and there exists a key in `x` with the same name as `key`, this function will attempt to
    construct an instance of `nested_data_class` from the value at `x[key]` and assign it to `x[key]`.
    If `x[key]` is a list, `nested_data_class` will be constructed for each item in the list.
    """
    if key is not None and nested_data_class is not None:
        value = x.pop(key)
        if isinstance(value, list):
            x[key] = [nested_data_class(**nested_item)
                      for nested_item in value]
        else:
            x[key] = nested_data_class(**value)
    return cls(**x)
