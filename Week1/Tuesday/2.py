#! /usr/bin/python
# Import sleep for delay at the end of the program.
from time import sleep
import turtle

# Initialize turtle class objects.
tr = turtle.Turtle(visible=False)
turtle.title("Turtle assigment Alfy")
turtle.screensize(200,200)

def tr_square(size, color="white"):
    tr.pendown()
    tr.fillcolor(color)
    tr.begin_fill()
    for i in range(4):
        tr.forward(size)
        tr.left(90)
    tr.end_fill()
    tr.penup()

def tr_triangle(size, color="white"):
    tr.pendown()
    tr.fillcolor(color)
    tr.begin_fill()
    for i in range(3):
        tr.forward(size)
        tr.left(120)
    tr.end_fill()
    tr.penup()

def tr_circle(size, color="white", radius=360):
    tr.pendown()
    tr.fillcolor(color)
    tr.begin_fill()
    tr.circle(size, radius)
    tr.end_fill()
    tr.penup()

if (__name__ == "__main__"):
    # Draw the head.
    tr_square(100, "brown")
    # Move to the top left corner of the head.
    tr.goto(0,100)
    # Draw left ear.
    tr_circle(35, "brown")
    tr_circle(25, "pink")
    # Move to the top right end of the head.
    tr.goto(100, 100)
    # Draw right ear.
    tr_circle(35, "brown")
    tr_circle(25, "pink")
    # Move to the left eye position.
    tr.goto(25,65)
    # Draw left eye.
    tr_circle(10)
    tr.goto(25,70)
    tr_circle(5, "black")
    # Move to the right eye position.
    tr.goto(75,65)
    # Draw right eye.
    tr_circle(10)
    tr.goto(75,70)
    tr_circle(5, "black")
    # Move to the nose position.
    tr.goto(45,55)
    # Draw nose.
    tr_triangle(10, "pink")
    # Move to the mouth position.
    tr.goto(30,35)
    # Rotate cursor for correct drawing start position.
    tr.right(90)
    # Draw the mouth.
    tr_circle(20, radius=180)
    # Move to the text position.
    tr.goto(0,-15)
    # Write text
    tr.write("Hello Word!")
    # Wait 5 sec before closing program.
    sleep(5)
