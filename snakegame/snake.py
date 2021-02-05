import turtle
import random as r
import time as t
wn = turtle.Screen()
wn.title("slitherio but worse")
wn.bgpic("cuhh.png")
wn.setup(width=1000, height=800)
wn.tracer(0)

score = 0
hs = 0
delay = 0.1

# Snake Head
snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("#2F11B3")
snakeHead.penup()
snakeHead.setx(0)
snakeHead.sety(0)
snakeHead.direction = "stop"

# Pen thing that does stuff 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center",
          font=("Courier New", 24, "normal"))

# movement


def movement():
    if(snakeHead.direction == "up"):
        y = snakeHead.ycor() + 20
        snakeHead.sety(y)
        print(
            "c,p[;c.,c c c")

    if(snakeHead.direction == "down"):
        y = snakeHead.ycor() - 20
        snakeHead.sety(y)
        print("hijksagdfghkjlsdf")

    if(snakeHead.direction == "left"):
        x = snakeHead.xcor() - 20
        snakeHead.setx(x)
        print("askoalsd;a;aslas;")

    if(snakeHead.direction == "right"):
        x = snakeHead.xcor() + 20
        snakeHead.setx(x)
        print("asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf")


def up():
    if(snakeHead.direction != "down"):
        snakeHead.direction = "up"


def down():
    if(snakeHead.direction != "up"):
        snakeHead.direction = "down"
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


def left():
    if(snakeHead.direction != "right"):
        snakeHead.direction = "left"


def right():
    if(snakeHead.direction != "left"):
        snakeHead.direction = "right"


# FOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("#FF2244")
food.penup()
food.shapesize(0.5, 0.5)
food.goto(100, 100)


bodies = []


wn.listen()
wn.onkey(up, "w")
wn.onkey(left, "a")
wn.onkey(down, "s")
wn.onkey(right, "d")

# Endless loop of pain
while True:
    wn.update()
    movement()
    t.sleep(delay)

    pen.clear()
    pen.write("Score: {} High Score: {}".format(
        score, hs), align="center", font=("Courier New", 24, "normal"))

    if(snakeHead.distance(food) < 15):
        x = r.randint(-280, 280)
        y = r.randint(-280, 280)
        food.goto(x, y)
        newBody = turtle.Turtle()
        newBody.speed(0)
        newBody.shape("square")
        newBody.color("#2F22B3")
        newBody.penup()
        bodies.append(newBody)
        score = score + 1
        if score > hs:
            hs = score

    for i in range(len(bodies)-1, 0, -1):
        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x, y)

    if(len(bodies) > 0):
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        bodies[0].goto(x, y)

    # collision with walls because you dont understand how the game works smh my head

    if snakeHead.xcor() > 600 or snakeHead.xcor() < -600 or snakeHead.ycor() > 390 or snakeHead.ycor() < -390:
        t.sleep(1)
        snakeHead.goto(0, 0)
        snakeHead.direction = "stop"
        for newBody in bodies:
            newBody.goto(1000, 2000)
        bodies = []
        score = 0

    # collision with literally anything else aka your tail
    for newBody in bodies:
        if(newBody.distance(snakeHead) < 5 and newBody != bodies[0]):
            t.sleep(0.5)
            snakeHead.goto(0, 0)
            snakeHead.direction = 'stop'
            for newBody in bodies:
                newBody.goto(1000, 2000)
            bodies = []
            score = 0
