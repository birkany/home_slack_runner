"""
This module will read the config.json and return requested values
if the value is not filled in, None will be returned.
"""
import json


def read_value(config_key: str):
    """
    Takes an input in the form of a key and then loads
    and reads the config json and returns the correct value
    :param config_key:  the key you want to find the value for, string.
    :return: value for the key given, string.
    """
    with open('config.json', 'rb') as config:
        config_dict = json.loads(config)
    return config_dict(config_key)
