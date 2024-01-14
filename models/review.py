#!/usr/bin/python3
"""Modele for class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class representaion of review"""
    place_id = ""
    user_id = ""
    text = ""
