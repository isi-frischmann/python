import turtle
# the distance we want the pointer to travel each time
# DIST = 200
# for x in range(5,10):
#     print "x", x
#     for y in range(6,10):
#         print "y", y
#         # turn the pointer 90 degrees to the right
#         turtle.right(90)
#         # advance according to set distance
#         turtle.forward(DIST)
#     # add to set distance
#     DIST += 20

# my_turtle = turtle.Turtle()
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.right(50)
# my_turtle.forward(70)
# my_turtle.left (50)

#Circle:
# turtle.speed(0)

# for i in range(50):
#     turtle.circle(5*i)
#     turtle.circle(-5*i)
#     turtle.left(i)
#     turtle.color("grey")

#star:
ob = turtle.Turtle()
ob.speed(10)

d = 100
angle = 140

for i in range(1, 100):
    ob.forward(d)
    ob.left(angle)
    d = d - 1

