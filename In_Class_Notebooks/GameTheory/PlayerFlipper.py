# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:34:34 2017

@author: shawla
"""

def move(history):
    mine, theirs = history
    if len(mine) % 2 == 0:
        return 'C'
    else:
        return 'D'