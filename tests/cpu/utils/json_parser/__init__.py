##!/usr/local/bin python3.10
# coding: utf-8
# File: __init__.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from .test_data_object import TestDataObject, create_test_data_object
from sample.cpu.utils import json_parser
import unittest
from unittest.mock import patch, mock_open, MagicMock, Mock