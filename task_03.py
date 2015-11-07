#! ur/bin/ env python
#-*- coding: utf- 8 -*-
"""Subclassing """


import produce

class Apple(produce.Produce):
    """Apple value update"""

    def __init__(self, duration):
        """Updated value of apple"""
        self.duration = '5356800'
    def duration(self):
        return self.duration

