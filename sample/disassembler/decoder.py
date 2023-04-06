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

    def read(self, address: int, count: int = 1):
        """
        Reads `count` bytes starting from `address`.

        Args: address: The address to start reading from.
            count: The number of bytes to read.

        Returns: The bytes read as an integer.

        Raises: IndexError: If the address is out of range.
        """

    def decode(self, address: int):
        """
        Decodes the instruction at `address`.

        Args: address: The address of the instruction to decode.
        
        Returns: A tuple containing the address of the next instruction and the decoded instruction.

        Raises: IndexError: If the address is out of range.
        """
