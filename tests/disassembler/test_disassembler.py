#!/usr/local/bin/python3.10
# coding: utf-8

from ..utils.mock import build_dataclass
from __init__ import *
import unittest
from unittest.mock import Mock, patch, MagicMock

from cpu.instruction import Instruction
from disassembler.disassembler import disassemble
from disassembler.decoder import Decoder
from cpu.operand import Operand


class TestDisassemble(unittest.TestCase):

    @patch('disassembler.decoder.Decoder.decode')
    def setUp(self, decoder_decode_fn_mocked) -> None:
        instruction_dict = {
            "immediate": True,
            "operands": [{
                "immediate": True,
                "name": "0",
                "bytes": None,
                "value": None,
                "adjust": None
            }, {
                "immediate": True,
                "name": "E",
                "bytes": None,
                "value": None,
                "adjust": None
            }],
            "cycles": [8],
            "bytes": 2,
            "mnemonic": "SET",
            "comment": "",
            "flags": {
                "Z": "-",
                "N": "-",
                "H": "-",
                "C": "-"}
        }
        instruction = build_dataclass(Instruction, instruction_dict, 'operands', Operand)
        self.decoder_decode_fn_mocked = decoder_decode_fn_mocked
        self.decoder_decode_fn_mocked.decode = Mock(return_value=(337, instruction))

        return super().setUp()

    @patch('builtins.print')
    def test_disassemble(self, mock_print):
        disassemble(self.decoder_decode_fn_mocked, 0x150, 1)
        mock_print.assert_called_with("0150 SET      0, E")

    #  TODO: Fix this test
    @patch('disassembler.decoder.Decoder.decode')
    def test_index_error(self, mock_decode):
        self.skipTest("Test not implemented")
