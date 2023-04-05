#!/usr/local/bin python3.10
# coding: utf-8
# File: instruction.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from .operand import Operand
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Instruction:
    immediate: bool
    operands: list[Operand]
    cycles: list[int]
    bytes: int
    mnemonic: str
    comment: str = ""
    flags: str = ""

    def from_dict(instruction_dict):
        """
            Create an Instruction object from a dictionary.

            Args:
                instruction_dict (dict): A dictionary containing the necessary information to create an Instruction object.

            Returns:
                Instruction: An Instruction object created from the given dictionary.
        """

    def copy(self, opcode: Optional[int] = None, immediate: Optional[bool] = None, operands: Optional[List[Operand]] = None, cycles: Optional[List[int]] = None, bytes: Optional[int] = None, mnemonic: Optional[str] = None, comment: Optional[str] = None, flags: Optional[str] = None) -> 'Instruction':
        """
        Creates a copy of the instruction, optionally replacing its opcode, mnemonic, or operands.
        """

    def print(self):
        """
        Prints a human-readable representation of the instruction.

        Returns:
            A string that contains the instruction's mnemonic and operands, and an optional comment.
        """
