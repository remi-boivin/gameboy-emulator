#!/usr/local/bin python3.10
# coding: utf-8

from .__init__ import *
import struct
import unittest
from hypothesis import given, strategies as st
from cartridge.cartridge import read_cartridge_metadata

HEADER_START = 0x100
HEADER_END = 0x14F
# Header size as measured from the last element to the first + 1
HEADER_SIZE = (HEADER_END - HEADER_START) + 1


class TestCartridge(unittest.TestCase):
    @given(data=st.binary(min_size=HEADER_SIZE + HEADER_START,
                          max_size=HEADER_SIZE + HEADER_START))
    def test_read_cartridge_metadata(self, data):
        def read(offset, count=1):
            return data[offset: offset + count + 1]

        metadata = read_cartridge_metadata(data)
        assert metadata.title == read(0x134, 14)
        checksum = read(0x14E, 2)
        # The checksum is in _big endian_ -- so we need to tell Python to
        # read it back in properly!
        assert metadata.global_checksum == int.from_bytes(
            checksum, sys.byteorder)
