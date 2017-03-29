# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:37:26 2017

@author: shawla
"""

def move(history):
    mine, theirs = history
    if len(theirs) > 0 and theirs[-1] == 'D':
        return 'D'
    else:
        return 'C'