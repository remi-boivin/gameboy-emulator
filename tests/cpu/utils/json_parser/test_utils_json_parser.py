##!/usr/local/bin python3.10
# coding: utf-8
# File: test_utils_json_parser.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from .__init__ import *


class TestJsonParser(unittest.TestCase):
    def test_json_parser_valid_data(self):
        expected_result = TestDataObject(username="Angelique", password="1234", email="angelique@gmail.com", age=21, country={"name": "Paris",
                                                                                                                              "code": "7502",
                                                                                                                              "address": "2 rue de la paix",
                                                                                                                              "city": "France"
                                                                                                                              })
        result = json_parser.json_parser(
            "./tests/cpu/utils/json_parser/datas/data.json", "Users", create_test_data_object)

        self.assertEqual(result["Angelique"], expected_result)

    @patch('builtins.print')
    def test_load_json_invalid_key(self, mock_print):
        result = json_parser.json_parser(
            "./tests/cpu/utils/json_parser/datas/invalid_data.json", "Users", create_test_data_object)
        mock_print.assert_called_with("Invalid Key: Users")

    @patch('builtins.print')
    def test_json_parser_invalid_path(self, mock_print):
        result = json_parser.json_parser(
            "./tests/cpu/utils/json_parser/datas/invalid_path.json", "Users", create_test_data_object)
        mock_print.assert_called_with(
            "File ./tests/cpu/utils/json_parser/datas/invalid_path.json not found")
