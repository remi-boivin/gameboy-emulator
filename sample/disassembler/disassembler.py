#!/usr/local/bin python3.10
# coding: utf-8
# File: test_instruction.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from .decoder import Decoder


def disassemble(decoder: Decoder, address: int, count: int) -> None:
    """
    Disassembles and prints out instructions starting from a given memory address.

    Args:
        decoder (Decoder): The decoder object to use for decoding instructions.
        address (int): The memory address of the first instruction to disassemble.
        count (int): The number of instructions to disassemble.

    Returns:
        None

    Raises: IndexError: If the address is out of range.
    """
    for _ in range(count):
        try:
            new_address, instruction = decoder.decode(address)
            pp = instruction.print()
            print(f'{address:>04X} {pp}')
            address = new_address
        except IndexError as e:
            print(f'ERROR - {e!s}')
            break
