#!/usr/bin/env python 

import turtle
from math import pi, cos, sin, atan2, sqrt
import math


# this will affect the fine-ness of the loops.
nsteps = 40

# create two turtle objects.
a = turtle.Turtle()
a.radians()

b = turtle.Turtle()
b.radians()

# set these to non-zero values 
# to watch the tracers, 
# or to 0, to see the full ting.
turtle.delay(0)
turtle.tracer(0)


def spirograph(ring_rad = 300, disk_rad = 125, hole_rad = 100):

  # Move turtle a -- the _disk_ center turtle
  # to its starting positions, with its pens up.  
  # When you're done with everything else, 
  # you can re-hide the "disk" turtle.
  
  # Move the turtle b -- the _hole_ turtle
  # to its starting positions, with its pen up.
  # Then put it back down.
  
  # CHALLENGE:
  # figure out how many loops you need, 
  # for the parameters given
  nloops = 200 

  th = 0 # disk angle.

  for loop in range(nloops):
    for step in range(nsteps):

      # Turtle 'a' should complete one circle every loop.
      # In other workds, 360 degrees, in nsteps.
      # Use fd/bk/left/right  commands to achieve that.
  
      # keep track of the angular position, th, of the large circle.
      # we actually need the full angle, not just mod 2pi,
      # since we are multiplying this by a funky fraction.
      # (In other words, we can't just ask the big turtle what
      #  his angle is.)
  
      # get the disk's position: ax, ay

      # use that position,
      # along with the sine/cosine from the assignment
      # to find the destination (bx, by) of the _hole_ turtle (b).

      # CHALLENGE: create a function to make a cool
      # radius or time-dependent color scheme.
      # colors are denoted by fractions of R, G, B.

      # now go to the new position.

  
# At least one call -- but get creative!!
spirograph()

# Leave this here to print your pretty picture.
turtle.getscreen().getcanvas().postscript(file="spirograph.eps")


