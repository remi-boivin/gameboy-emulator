#!/usr/local/bin python3.10
# coding: utf-8
# File: test_instruction.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from .__init__ import *
from cpu.instruction import Instruction
from cpu.operand import Operand
from hypothesis import given
import hypothesis.strategies as st


class TestInstruction(unittest.TestCase):
    operand = []
    operand1 = []
    operand.append(build_dataclass(
        Operand, {"immediate": True, "name": "BC", 'bytes': 3, 'value': 0, 'adjust': None}))
    operand1.append(build_dataclass(Operand, {
        "immediate": True, "name": "BC", 'bytes': 3, 'value': 12779520, 'adjust': None}))

    @patch('cpu.operand.Operand.from_dict', side_effect=[operand, operand1])
    def setUp(self, operand_from_dict_mocked) -> None:
        self.operands_dicts = [{"immediate": False, "name": "A", "bytes": 1, "value": None, "adjust": None}, {
            "immediate": False, "name": "A", "bytes": 1, "value": None, "adjust": None}]
        self.operands = Operand.from_dict(self.operands_dicts)
        return super().setUp()

    @given(st.lists(st.fixed_dictionaries({"immediate": st.booleans(),
                                           "operands": st.lists(st.fixed_dictionaries({"immediate": st.booleans(),
                                                                                      "name": st.text(),
                                                                                       "bytes": st.integers(min_value=1, max_value=200),
                                                                                       "value": st.one_of(st.integers(), st.none()),
                                                                                       "adjust": st.one_of(st.none(), st.text("+-"))
                                                                                       })),
                                           "cycles": st.lists(st.integers()), "bytes": st.integers(), "mnemonic": st.text(), "comment": st.text(), "flags": st.text()})))
    def test_from_dict(self, instruction_dicts):
        instructions = []

        for instruction_dict in instruction_dicts:
            instruction = Instruction.from_dict(instruction_dict)

            instructions.append(instruction)
            self.assertEqual(instruction.cycles, instruction_dict['cycles'])
            self.assertEqual(instruction.bytes, instruction_dict['bytes'])
            self.assertEqual(instruction.comment, instruction_dict['comment'])
            self.assertEqual(instruction.flags, instruction_dict['flags'])

    @patch('cpu.operand.Operand.from_dict', side_effect=operand1)
    @given(immediate=st.booleans(),
           operands=st.lists(st.text()),
           cycles=st.lists(st.integers()),
           bytes=st.integers(),
           mnemonic=st.text(),
           comment=st.text(),
           flags=st.text())
    def test_copy_with_no_values(self, immediate, operands, cycles, bytes, mnemonic, comment, flags, operand_copy_mocked):
        instr = Instruction(immediate=immediate, operands=operands, cycles=cycles,
                            bytes=bytes, mnemonic=mnemonic, comment=comment, flags=flags)
        self.assertEqual(instr, instr.copy())

    @patch('cpu.operand.Operand.from_dict', side_effect=operand1)
    @given(immediate=st.booleans(),
           operands=st.lists(st.text()),
           cycles=st.lists(st.integers()).filter(lambda x: x != [8]),
           bytes=st.integers(),
           mnemonic=st.text(),
           comment=st.text(),
           flags=st.text())
    def test_copy(self, immediate, operands, cycles, bytes, mnemonic, comment, flags, operand_from_dict_mocked):
        instr = Instruction(immediate=immediate, operands=operands, cycles=cycles,
                            bytes=bytes, mnemonic=mnemonic, comment=comment, flags=flags)
        instr_copy = instr.copy(opcode=0x0, immediate=False if immediate else True,
                                operands=self.operands[0], cycles=[8], bytes=bytes+5)
        self.assertNotEqual(instr.immediate, instr_copy.immediate)
        self.assertNotEqual(instr.operands, instr_copy.operands)
        self.assertNotEqual(instr.cycles, instr_copy.cycles)
        self.assertNotEqual(instr.bytes, instr_copy.bytes)
        self.assertEqual(instr.mnemonic, instr_copy.mnemonic)
        self.assertEqual(instr.comment, instr_copy.comment)

    def test_copy_missing_immediate(self):
        instruction = Instruction.from_dict(
            {'operands': [], 'cycles': [], 'bytes': 0, 'mnemonic': 'test'})
        self.assertEqual(instruction.immediate, None)

    def test_copy_missing_cycles(self):
        instruction = Instruction.from_dict(
            {'immediate': False, 'operands': [], 'bytes': 0, 'mnemonic': 'test'})
        self.assertEqual(instruction.cycles, None)

    def test_copy_missing_bytes(self):
        instruction = Instruction.from_dict(
            {'immediate': False, 'operands': [], 'cycles': [], 'mnemonic': 'test'})
        self.assertEqual(instruction.bytes, None)

    def test_copy_missing_mnemonic(self):
        instruction = Instruction.from_dict(
            {'immediate': False, 'operands': [], 'cycles': [], 'bytes': 0})
        self.assertEqual(instruction.mnemonic, None)

    def test_print(self):
        instruction = Instruction.from_dict(
            {'immediate': False, 'operands': [], 'cycles': [], 'bytes': 0, 'mnemonic': 'test', 'comment': 'test'})
        self.assertEqual(str(instruction.print()), 'test      ; test      ')
