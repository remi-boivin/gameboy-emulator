#!/usr/local/bin python3.10
# coding: utf-8
# File: test_instruction.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from ..utils.mock import mock_fn, build_dataclass

from __init__ import *
import unittest
from unittest.mock import patch
from disassembler.decoder import Decoder
from cpu.instruction import Instruction
from cpu.operand import Operand


operand = build_dataclass(
    Operand, {"immediate": True, "name": "BC", 'bytes': 3, 'value': 0, 'adjust': None})
operand1 = build_dataclass(Operand, {
                           "immediate": True, "name": "BC", 'bytes': 3, 'value': 12779520, 'adjust': None})


class TestDecode(unittest.TestCase):

    @patch('disassembler.decoder.Decoder.create')
    def setUp(self, create_decoder_mocked) -> None:
        instruction_dict = {"immediate": True, "operands": [
            {"immediate": True, "name": "BC", 'bytes': 3,
             'value': None, 'adjust': None},
            {"immediate": True, "name": "BC", 'bytes': 3, 'value': None, 'adjust': None}], "cycles": [12], "bytes": 3, "mnemonic": "LD", "flags": "Z"}

        prefixed_instruction_dict = {"immediate": True, "operands": [
            {"immediate": True, "name": "B", 'bytes': 3,
             'value': None, 'adjust': None}], "cycles": [12], "bytes": 3, "mnemonic": "RLC", "flags": "Z"}

        expected_instruction_dict = {"immediate": True, "operands": [
            {"immediate": True, "name": "BC", 'bytes': 3,
             'value': 0, 'adjust': None},
            {"immediate": True, "name": "BC", 'bytes': 3, 'value': 12779520, 'adjust': None}], "cycles": [12], "bytes": 3, "mnemonic": "LD", "flags": "Z"}

        self.expected_instruction = build_dataclass(
            Instruction, expected_instruction_dict, "operands", Operand)

        self.instruction = {
            0x01: build_dataclass(
                Instruction, instruction_dict, "operands", Operand),
        }

        self.prefixed_instruction = {
            0x01: build_dataclass(
                Instruction, prefixed_instruction_dict, "operands", Operand),
        }
        with open("data/super_mario.gb", "rb") as opcode_file:
            self.binary_opcode = opcode_file.read()
        create_decoder_mocked.return_value = Decoder(
            prefixed_instructions=self.prefixed_instruction, instructions=self.instruction, data=self.binary_opcode, address=0x00)
        self.decoder = Decoder.create(
            "data/optcodes.json", self.binary_opcode, b"\x00")
        return super().setUp()

    @patch('disassembler.decoder.load_opcodes')
    def test_create(self, mock_load_opcodes_fn):
        mock_load_opcodes_fn.return_value = self.prefixed_instruction, self.instruction
        decoder = Decoder.create("data/optcodes.json",
                                 self.binary_opcode, b"\x00")
        expected_decoder = Decoder(
            self.binary_opcode, b"\x00", self.prefixed_instruction, self.instruction)
        self.assertEqual(
            decoder, expected_decoder)
        mock_load_opcodes_fn.assert_called_once_with('data/optcodes.json')

    @patch('cpu.operand.Operand.copy', side_effect=[operand, operand1])
    def test_decode_valid_address_instructions(self, mock_operand_copy_fn):
        decoded_instruction = self.decoder.decode(0x02)
        self.assertEqual(
            decoded_instruction[1], self.expected_instruction)

    def test_decode_prefixed_instruction(self):
        decoder = Decoder.create(
            opcode_file="data/optcodes.json",
            data=b"",  # pass empty bytes as we are mocking read()
            address=0
        )
        with patch.object(Decoder, 'read') as mock_read:
            # Set up the mock to return the appropriate opcode bytes
            mock_read.side_effect = [0xCB, 0x01, 0x00, 0x00]
            # Decode the instruction at address 0
            address = 0
            decoded_address, decoded_instruction = decoder.decode(address)
            # Check that the instruction was decoded correctly
            print(decoded_instruction)
            self.assertEqual(decoded_address, 2)
            self.assertEqual(decoded_instruction.mnemonic, "RLC")
            self.assertEqual(len(decoded_instruction.operands), 1)
            self.assertEqual(decoded_instruction.operands[0].name, "C")

    def test_decode_invalid_instruction(self):
        decoder = Decoder.create(
            opcode_file="data/optcodes.json",
            data=b"",  # pass empty bytes as we are mocking read()
            address=0
        )
        with patch.object(Decoder, 'read') as mock_read:
            # Set up the mock to return the appropriate opcode bytes
            mock_read.side_effect = [0x00, 0x00, 0x00, 0x00]
            # Decode the instruction at address 0
            address = 0
            with self.assertRaises(IndexError):
                decoder.decode(address)

    def test_read_valid_address(self):
        self.assertEqual(self.decoder.read(2), 1)
        self.assertEqual(self.decoder.read(3, 2), 0)

    def test_read_invalid_address(self):
        with self.assertRaises(IndexError):
            self.decoder.read(100000)

    @patch('builtins.print')
    def test_invalid_adress_instruction(self, print_mocked_method):
        address = 0x100000

        with self.assertRaises(IndexError):
            self.decoder.decode(address)
            print_mocked_method.assert_called_with(
                f"IndexError: address={address}+count=1 is out of range")
