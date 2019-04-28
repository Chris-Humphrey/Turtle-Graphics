from turtle import *

## CREATE FUNCTIONS FOR EACH SHAPE

# TRIANGLE
def tri():
    for i in range(3):
        forward(150)
        right(120)
    # mainloop()

# SQUARE
def squ():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    # mainloop()

# PENTAGON
def pen():
    for i in range(5):
        forward(100)
        right(72)
    # mainloop()

# HEXAGON
def hex():
    for i in range(6):
        forward(100)
        right(60) 
    # mainloop()

# OCTAGON
def oct():
    for i in range(8):
        forward(100)
        right(45)  
    # mainloop()

# STAR
def sta():
    for i in range(5):
        forward(100)
        right(144)
    # mainloop()

# CIRCLE
def cir():
    circle(160)

tri()
squ()
pen()
hex()
oct()
sta()
cir()