#!/usr/local/bin python3.10
# coding: utf-8
# File: test_instruction.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

def read_cartridge_metadata(buffer, offset: int = 0x100):
    """
    Unpacks the cartridge metadata from `buffer` at `offset` and
    returns a `CartridgeMetadata` object.
    """