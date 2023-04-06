#!/usr/local/bin python3.10
# coding: utf-8
# File: test_instruction.py
# Project: Python Gameboy emulator
# File Created: Thurday, 6th April 2023

import json
from __init__ import *
from cpu.instruction import Instruction


def load_opcodes(opcode_file: str) -> dict:
    """
    Load the instruction set from the given opcode_file.
    Args: opcode_file (str): The path to the opcode file.
    Returns: A dictionary of instructions.
    Raises: FileNotFoundError: If the given opcode_file does not exist.
    """
