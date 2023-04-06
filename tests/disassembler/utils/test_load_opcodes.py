#!/usr/local/bin python3.10
# coding: utf-8
# File: test_instruction.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 6th April 2023

import json
from ...utils.mock import mock_fn, build_dataclass
import unittest
from unittest.mock import patch

from __init__ import *
from disassembler.utils.opcodes import load_opcodes
from cpu.instruction import Instruction
from cpu.operand import Operand


instruction_dict = {"immediate": True, "operands": [
    {"immediate": True, "name": "BC", 'bytes': 3,
     'value': None, 'adjust': None},
    {"immediate": True, "name": "BC", 'bytes': 3, 'value': None, 'adjust': None}], "cycles": [12], "bytes": 3, "mnemonic": "LD", "flags": "Z"}

prefixed_instruction_dict = {"immediate": True, "operands": [
    {"immediate": True, "name": "B", 'bytes': 3,
     'value': None, 'adjust': None}], "cycles": [12], "bytes": 3, "mnemonic": "RLC", "flags": "Z"}

instruction = build_dataclass(
    Instruction, instruction_dict, "operands", Operand)
prefixed_instruction = build_dataclass(
    Instruction, prefixed_instruction_dict, "operands", Operand)

operands = []
prefixed_operands = []

operands.append(build_dataclass(
    Operand, {"immediate": True, "name": "BC", 'bytes': 3,
     'value': None, 'adjust': None}))
# operand1 = build_dataclass(
#     Operand, instruction_dict["operands"][1])

prefixed_operands.append(build_dataclass(
    Operand, {"immediate": True, "name": "B", 'bytes': 3,'value': None, 'adjust': None}))


class TestLoadOpcodes(unittest.TestCase):

    def setUp(self):
        self.test_opcodes_file = "test_opcodes.json"
        self.invalid_file = "invalid_file.json"
        self.sample_data = {
            "unprefixed": {
                "00": {
                    "mnemonic": "NOP",
                    "bytes": 1,
                    "cycles": 4
                }
            },
            "cbprefixed": {
                "00": {
                    "mnemonic": "RLC B",
                    "bytes": 2,
                    "cycles": 8
                }
            }
        }
        with open(self.test_opcodes_file, "w") as f:
            json.dump(self.sample_data, f)

    def test_load_opcodes_valid_file(self):
        prefixed, regular = load_opcodes(self.test_opcodes_file)
        self.assertIsInstance(prefixed, dict)
        self.assertIsInstance(regular, dict)
        self.assertEqual(len(prefixed), 1)
        self.assertEqual(len(regular), 1)
        self.assertIsInstance(prefixed[0], Instruction)
        self.assertIsInstance(regular[0], Instruction)

    def test_load_opcodes_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            load_opcodes(self.invalid_file)
