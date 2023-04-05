#!/usr/local/bin python3.10
# coding: utf-8
# File: operand.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from dataclasses import dataclass
from typing import List, Optional, Literal


@dataclass(frozen=True)
class Operand:

    immediate: bool
    name: str
    bytes: int
    value: int | None
    adjust: Literal["+", "-"] | None

    def create(**kwargs):
        """
        Create an Operand object from keyword arguments.

        Args:
            **kwargs: Keyword arguments to pass to the Operand constructor.

        Returns:
            Operand: An Operand object created from the given keyword arguments.
        """
        return Operand(immediate=kwargs.get('immediate'), name=kwargs.get('name'), bytes=kwargs.get('bytes'), value=kwargs.get('value'), adjust=kwargs.get('adjust'))

    @staticmethod
    def from_dict(operand_dict):
        """
        Create a list of operands from a dictionary representation.

        Args:
            operand_dict (dict): A dictionary representation of the operands.

        Returns:
            list: A list of Operand objects.

        Exceptions:
            TypeError: If the dictionary is empty or if the values are of the wrong type.
        """
        try:
            operands = []
            for operand in operand_dict:
                operands.append(Operand.create(name=operand.get('name'),
                                               immediate=operand.get(
                    'immediate'),
                    bytes=operand.get(
                    'bytes'),
                    value=operand.get(
                    'value'),
                    adjust=operand.get(
                    'adjust')))
            return operands
        except TypeError as e:
            print(e)
            return []

    def copy(self, value=None, adjust=None):
        """
        Creates a copy of this Operand object, with optional value and adjust arguments.

        Args:
            value (int): Optional new value for the Operand.
            adjust (int): Optional new adjust value for the Operand.

        Returns:
            An Operand object with the same attributes as this Operand, except for any specified in the arguments.
        """
        if value is not None:
            return Operand(immediate=self.immediate,
                           name=self.name,
                           bytes=self.bytes,
                           value=value,
                           adjust=adjust)
        else:
            return Operand(immediate=self.immediate,
                           name=self.name,
                           bytes=self.bytes,
                           value=self.value,
                           adjust=adjust)

    def print(self):
        """
        Prints a human-readable representation of the Operand object.

        Returns:
            str: A string representation of the Operand object.
        """
        try:
            if self.adjust is None:
                adjust = ""
            else:
                adjust = self.adjust
            if self.value is not None:
                if self.bytes is not None:
                    val = hex(self.value)
                else:
                    val = self.value
                v = val
            else:
                v = self.name
            v = v + adjust
            if self.immediate:
                return v
            return f'({abs(v)})'
        except TypeError as e:
            print(e)
            return ""
