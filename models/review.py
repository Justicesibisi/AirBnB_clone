#!/usr/bin/python3
"""A module to create review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class=managing review objects"""
    place_id = ""
    user_id = ""
    text = ""
