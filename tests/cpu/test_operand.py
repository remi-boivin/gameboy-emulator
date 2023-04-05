#!/usr/local/bin python3.10
# coding: utf-8
# File: operand.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from hypothesis import given
import hypothesis.strategies as st
from sample.cpu.operand import Operand
import unittest
from unittest.mock import patch
from ..utils.mock import build_dataclass


class TestOperand(unittest.TestCase):
    operand = []
    operand1 = []
    operand.append(build_dataclass(
        Operand, {"immediate": True, "name": "BC", 'bytes': 3, 'value': 0, 'adjust': None}))
    operand1.append(build_dataclass(Operand, {
        "immediate": True, "name": "BC", 'bytes': 3, 'value': 12779520, 'adjust': None}))

    @patch('sample.cpu.operand.Operand.from_dict', side_effect=[operand, operand1])
    def setUp(self, operand_from_dict_mocked) -> None:
        self.operands_dicts = [{"immediate": False, "name": "A", "bytes": 1, "value": None, "adjust": None}, {
            "immediate": False, "name": "A", "bytes": 1, "value": None, "adjust": None}]
        self.operands = Operand.from_dict(self.operands_dicts)
        return super().setUp()

    def test_from_dict(self):
        operands = Operand.from_dict(self.operands_dicts)

        if self.operands_dicts.__len__() == 0:
            self.assertEqual(operands, [])
        else:
            for operands_dict, operand in zip(self.operands_dicts, operands):
                self.assertEqual(operand.name, operands_dict['name'])
                self.assertEqual(operand.value, operands_dict['value'])
                self.assertEqual(operand.adjust, operands_dict['adjust'])
                self.assertEqual(operand.immediate, operands_dict['immediate'])
                self.assertEqual(operand.bytes, operands_dict['bytes'])

    def test_from_dict_bis(self):
        self.assertEqual(Operand.from_dict(None), [])

    def test_copy(self):
        for operand in self.operands:
            operand_copy = operand.copy(
                value=operand.value + 895) if operand.value is not None else operand.copy(value=78)
            self.assertEqual(operand.immediate, operand_copy.immediate)
            self.assertEqual(operand.name, operand_copy.name)
            self.assertEqual(operand.bytes, operand_copy.bytes)
            self.assertEqual(operand.adjust, operand_copy.adjust)
            self.assertNotEqual(operand.value, operand_copy.value)
            self.assertNotEqual(operand, operand_copy)

    def test_empty_value_copy(self):
        for operand in self.operands:
            operand_copy = operand.copy()
            self.assertEqual(operand, operand_copy)

    def test_print_bis(self):
        for operand in self.operands:
            result = operand.print()
            self.assertEqual(result, str(hex(operand.value)))

    def test_negative_adjustment(self):
        operand = Operand(
            immediate=False, name="HL", bytes=2, value=0x1234, adjust=-11)
        self.assertEqual(operand.print(), '')
