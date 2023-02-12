#!/usr/bin/python3
"""the shebang"""
import json


def load_from_json_file(filename):
    """Create an onject from a JSON file"""
    with open(filename) as f:
        return json.load(f)
