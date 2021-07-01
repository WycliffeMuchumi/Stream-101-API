import re
from flask import make_response, jsonify

"""
    Validates key-value pairs of request dictionary body.
"""
def validate_users_key_pair_values(request):
    keys = ['firstName','lastName','userName','email','phoneNumber','password']
    errors = []
    for key in keys:
        if key not in request.json:
            errors.append(key)
    return errors

"""
    Validates key-value pairs of request dictionary body.
"""
def validate_videos_key_pair_values(request):
    keys = ['title','description','video_content']
    errors = []
    for key in keys:
        if key not in request.json:
            errors.append(key)
    return errors


def check_for_blanks(data):
    blanks = []
    for key, value in data.items():
        if value == "":
            blanks.append(key)
    return blanks


def check_for_non_strings(data):
    non_strings = []
    for key, value in data.items():
        if key != 'id' and not isinstance(value, str):
            non_strings.append(key)
    return non_strings


def check_for_non_ints(data):
    non_ints = []
    for key, value in data.items():
        if not isinstance(value, int):
            non_ints.append(key)
    return non_ints