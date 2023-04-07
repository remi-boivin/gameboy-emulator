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

    try:
        with open(opcode_file) as f:
            data = json.load(f)
        prefixed_instructions = {}
        regular_instructions = {}

        for opcode_str, instruction_dict in data["unprefixed"].items():
            opcode = int(opcode_str, 16)
            regular_instructions[opcode] = Instruction.from_dict(
                instruction_dict)

        for opcode_str, instruction_dict in data["cbprefixed"].items():
            opcode = int(opcode_str, 16)
            prefixed_instructions[opcode] = Instruction.from_dict(
                instruction_dict)
        return prefixed_instructions, regular_instructions
    except FileNotFoundError as e:
        print(f'ERROR - {e!s}')
        raise e
