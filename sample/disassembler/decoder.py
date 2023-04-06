#!/usr/local/bin python3.10
# coding: utf-8
# File: test_instruction.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from __init__ import *
from opcodes import load_opcodes
from dataclasses import dataclass
import sys


@dataclass
class Decoder:

    data: bytes
    address: int
    prefixed_instructions: dict
    instructions: dict

    @classmethod
    def create(cls, opcode_file: str, data: bytes, address: int = 0):
        """
        Load the opcodes from the opcode file and creates a new `Decoder` instance.

        Args: cls: The class to create an instance of.
            opcode_file: The path to the opcode file.
            data: The data to decode.
            address: The address to start decoding at.

        Returns: A new `Decoder` instance.
        """
        prefixed, regular = load_opcodes(opcode_file)
        return cls(
            prefixed_instructions=prefixed,
            instructions=regular,
            data=data,
            address=address,
        )

    def read(self, address: int, count: int = 1):
        """
        Reads `count` bytes starting from `address`.

        Args: address: The address to start reading from.
            count: The number of bytes to read.

        Returns: The bytes read as an integer.

        Raises: IndexError: If the address is out of range.
        """
        if 0 <= address + count <= len(self.data):
            v = self.data[address: address + count]
            return int.from_bytes(v, sys.byteorder)
        else:
            raise IndexError(f'{address=}+{count=} is out of range')

    def decode(self, address: int):
        """
        Decodes the instruction at `address`.

        Args: address: The address of the instruction to decode.
        
        Returns: A tuple containing the address of the next instruction and the decoded instruction.

        Raises: IndexError: If the address is out of range.
        """
        opcode = None
        decoded_instruction = None
        opcode = self.read(address)
        if opcode == 0x00:
            raise IndexError(f'{address=} is out of range')
        address += 1
        # 0xCB is a special prefix instruction. Read from
        # prefixed_instructions instead and increment address.
        if opcode == 0xCB:
            opcode = self.read(address)
            address += 1
            instruction = self.prefixed_instructions[opcode]
        else:
            instruction = self.instructions[opcode]
        new_operands = []
        for operand in instruction.operands:
            if operand.bytes is not None:
                value = self.read(address, operand.bytes)
                address += operand.bytes
                new_operands.append(operand.copy(value))
            else:
                # No bytes; that means it's not a memory address
                new_operands.append(operand)
        decoded_instruction = instruction.copy(operands=new_operands)
        return address, decoded_instruction
