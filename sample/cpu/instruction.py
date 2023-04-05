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
        instruction = Instruction(
            immediate=instruction_dict.get('immediate'),
            operands=Operand.from_dict(instruction_dict.get('operands')),
            cycles=instruction_dict.get('cycles'),
            bytes=instruction_dict.get('bytes'),
            mnemonic=instruction_dict.get('mnemonic'),
            comment=instruction_dict.get('comment', ''),
            flags=instruction_dict.get('flags', ''))
        return instruction

    def copy(self, opcode: Optional[int] = None, immediate: Optional[bool] = None, operands: Optional[List[Operand]] = None, cycles: Optional[List[int]] = None, bytes: Optional[int] = None, mnemonic: Optional[str] = None, comment: Optional[str] = None, flags: Optional[str] = None) -> 'Instruction':
        """
        Creates a copy of the instruction, optionally replacing its opcode, mnemonic, or operands.
        """
        return Instruction(immediate=immediate if immediate is not None else self.immediate,
                           operands=operands if operands is not None else self.operands.copy(),
                           cycles=cycles if cycles is not None else self.cycles,
                           bytes=bytes if bytes is not None else self.bytes,
                           mnemonic=mnemonic if mnemonic is not None else self.mnemonic,
                           comment=comment if comment is not None else self.comment,
                           flags=flags if flags is not None else self.flags)

    def print(self):
        """
        Prints a human-readable representation of the instruction.

        Returns:
            A string that contains the instruction's mnemonic and operands, and an optional comment.
        """
        ops = ', '.join(op.print() for op in self.operands)
        s = f"{self.mnemonic:<8} {ops}"
        if self.comment:
            s = s + f" ; {self.comment:<10}"
        return s
