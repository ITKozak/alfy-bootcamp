#! /usr/bin/python

import turtle

def triangle(edge=100):
    # The problem was that we have had one extra side to draw
    # and that we dont start drawing the next triangle.
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    # By rotating by 180 degree we point "turtle" to draw the next
    # next triangle in the next itteration.
    turtle.right(180)

if (__name__ == "__main__"):
    for i in range(6):
        triangle()