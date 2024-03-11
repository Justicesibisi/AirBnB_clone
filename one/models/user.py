#!/usr/bin/python3
"""This module creates User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing users objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""i
