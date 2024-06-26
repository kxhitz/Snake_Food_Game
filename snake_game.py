import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0

bodies = []

# Set up the screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("powderblue")
s.setup(width=600, height=600)
s.tracer(0)  # Turn off automatic screen updates

# Add a border to the game area
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-290, -290)
border.pendown()
border.pensize(3)
for _ in range(4):
    border.forward(580)
    border.left(90)
border.hideturtle()

# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Create the food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# Create the score display
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("white")
sb.penup()
sb.ht()
sb.goto(0, 260)
sb.write("Score: 0 | Highest Score: 0", align="center", font=("Courier", 16, "normal"))

def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def movestop():
    head.direction = "Stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    s.update()

s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

while True:
    s.update()

    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)
        score += 10
        delay -= 0.001
        if score > highestscore:
            highestscore = score
        sb.clear()
        sb.write("Score: {} | Highest Score: {}".format(score, highestscore), align="center",
                 font=("Courier", 16, "normal"))

    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            for b in bodies:
                b.ht()
            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: {} | Highest Score: {}".format(score, highestscore), align="center",
                     font=("Courier", 16, "normal"))
    time.sleep(delay)
turtle.mainloop()