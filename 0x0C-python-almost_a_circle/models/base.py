#!/usr/bin/python3
"""Defines a class Base"""
import json
import os.path
import csv
import turtle


class Base:
    """Class that defines properties of a base

    Attributes:
        id(int): identity of each integer
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Creates new instances of base.

        Args:
            id(int):Identity of each instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = Base.__nb_objects
