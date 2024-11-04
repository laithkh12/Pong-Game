from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
import time
from ScoreBoard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

rightPaddle = Paddle((350,  0))
leftPaddle = Paddle((-350, 0))
ball = Ball()
scoreBoard = ScoreBoard()


screen.listen()
screen.onkey(rightPaddle.goUp(), "Up")
screen.onkey(rightPaddle.goDown(), "Down")

screen.onkey(leftPaddle.goUp(), "w")
screen.onkey(leftPaddle.goDown(), "s")

gameIsOn = True
while gameIsOn:

    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounceY()

    # Detect collision with paddle
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    # Detect right paddle missed
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreBoard.lScore()

    # Detect left paddle missed
    if ball.xcor() < -380:
        ball.resetPosition()
        scoreBoard.rScore()






screen.exitonclick()