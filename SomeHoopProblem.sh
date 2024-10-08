#!/bin/bash

# d can be anything
# L can deffo be anything
# d being diameter indicates diameter, radius, or area might
# be used to find probability.
# We are going to be assuming the coin can indeed be touching one
# colour if thrown (hence it is not too big)
# We draw out the maxium area that the circle can be in
# The area is square like, after all it is enclosed by a 
# bigger square. Hence we could take the centre of the hoop.
# The hoop is place in many positions in one square, and it
# only touches one colour in that square.
# Drawing it out on a whiteboard, I see that by taking the centre
# of the many circles drawn in their maximum position, it forms
# a square. The area of this square is d^2. The area of the
# surrounding square is L^2.
# Hence the probability of falling in 1 colour is:
# (L^2 - d^2) / (L^2)
# Hence 1 - ThatAbove is the probability of hoop in 2 colors.
