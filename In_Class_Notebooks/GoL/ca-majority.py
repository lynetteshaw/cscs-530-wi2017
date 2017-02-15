# Simple CA simulator in Python
#
# *** Majority Rule ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 50
height = 50
numberOfStates = 2
r = 1

def init():
    global time, config, nextConfig

    time = 0
    
    config = SP.zeros([height, width])
    for x in xrange(width):
        for y in xrange(height):
            state = RD.randint(0, numberOfStates - 1)
            config[y, x] = state

    nextConfig = SP.zeros([height, width])

def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = numberOfStates - 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, config, nextConfig

    time += 1

    for x in xrange(width):
        for y in xrange(height):
            state = config[y, x]
            counts = [0] * numberOfStates
            for dx in xrange(- r, r + 1):
                for dy in xrange(- r, r + 1):
                    s = int(config[(y+dy)%height, (x+dx)%width])
                    counts[s] += 1
            maxCount = max(counts)
            maxStates = []
            for i in xrange(numberOfStates):
                if counts[i] == maxCount:
                    maxStates.append(i)
            state = RD.choice(maxStates)
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
