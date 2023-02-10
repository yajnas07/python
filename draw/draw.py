import turtle
t = turtle.Turtle()
  
# taking input for the no of the sides of the polygon
n = int(input("Enter the no of the sides of the polygon : "))
  
# taking input for the length of the sides of the polygon
l = int(input("Enter the length of the sides of the polygon : "))
  
  
for i in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
    
n = input("press any key o exit ")
