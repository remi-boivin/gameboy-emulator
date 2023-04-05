##!/usr/local/bin python3.10
# coding: utf-8
# File: json_parser.py
# Project: Python Gameboy emulator
# File Created: Wednesday, 5th April 2023

import json


def json_parser(file_path, set_key, factory_func, *args, **kwargs):
    """
    Parses a JSON file containing a set of data, creates an data object for each
    data in the set using a factory function, and returns a dictionary of data objects.

    Args:
        file_path (str): The file path of the JSON file to parse.
        set_key (str): The key of the dictionary containing the set of data in the JSON file.
        factory_func (function): A function that creates data objects based on an key and
            a dictionary of parameters. The function should take at least two arguments: the key
            and the dictionary of parameters. Any additional arguments or keyword arguments can be
            passed in as optional arguments to `json_parser`, and will be passed along to
            the factory function.
        *args: Any additional positional arguments to pass to the factory function.
        **kwargs: Any additional keyword arguments to pass to the factory function.

    Returns:
        dict: A dictionary of data objects, where the keys are the keys and the values
            are the data objects created by the factory function.

    Raises:
        FileNotFoundError: If the specified file path does not exist or cannot be opened.

    """
    dataset = {}

    try:
        with open(file_path) as file:
            tmp = json.load(file)
            try:
                for key, params in tmp[set_key].items():
                    data = factory_func(key, params, *args, **kwargs)
                    dataset[key] = data
            except KeyError:
                print("Invalid Key: " + set_key)
        return dataset
    except FileNotFoundError:
        print(f"File {file_path} not found")
