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

    def copy(self, value=None, adjust=None):
        """
        Creates a copy of this Operand object, with optional value and adjust arguments.

        Args:
            value (int): Optional new value for the Operand.
            adjust (int): Optional new adjust value for the Operand.

        Returns:
            An Operand object with the same attributes as this Operand, except for any specified in the arguments.
        """

    def print(self):
        """
        Prints a human-readable representation of the Operand object.

        Returns:
            str: A string representation of the Operand object.
        """
