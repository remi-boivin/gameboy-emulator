#!/usr/local/bin python3.10
# coding: utf-8
# File: __init__.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023
import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '../../sample')
sys.path.append(mymodule_dir)
