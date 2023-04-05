##!/usr/local/bin python3.10
# coding: utf-8
# File: __init__.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

from dataclasses import dataclass

@dataclass
class TestDataObject():

    username: str
    password: str
    email: str
    age: int
    country: dict

def create_test_data_object(username, params):
    return TestDataObject(username=username,
                          password=params['password'],
                          email=params['email'],
                          age=params['age'],
                          country=params['country'])
