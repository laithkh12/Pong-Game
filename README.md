# 🏓 Pong Game

A classic Pong game built in Python using the Turtle graphics library. Play against an opponent, keep the ball in play, and see who scores the most points! 🎮

## 📋 Table of Contents
- [✨ Features](#-features)
- [📂 Code Overview](#-code-overview)
  - [main.py](#mainpy)
  - [paddle.py](#paddlepy)
  - [ball.py](#ballpy)
  - [scoreboard.py](#scoreboardpy)
- [⚙️ Requirements](#️-requirements)
- [▶️ How to Run](#️-how-to-run)
- [📄 License](#-license)

## ✨ Features
- **Player Controls** - Move the paddles up and down with specific keys (`Up/Down` for Player 1, `W/S` for Player 2).
- **Score Tracking** - Scores are displayed at the top, updating each time a player misses the ball.
- **Realistic Ball Bouncing** - Ball bounces off walls and paddles, increasing in speed with each paddle bounce.
- **Game Screen** - 800x600 pixels with a black background for a retro arcade feel.

## 📂 Code Overview

### main.py
The main script initializes the game environment and manages the core game loop.

- **Screen Setup**: An 800x600 black screen titled "Pong Game".
- **Game Elements**: Creates instances of `Paddle`, `Ball`, and `ScoreBoard`.
- **Key Bindings**: Maps the Up and Down arrow keys to the right paddle and W/S keys to the left paddle.
- **Game Loop**: Continuously updates the screen, moves the ball, detects collisions, and tracks scoring.

```python
from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Initialize paddles, ball, and scoreboard
rightPaddle = Paddle((350, 0))
leftPaddle = Paddle((-350, 0))
ball = Ball()
scoreBoard = ScoreBoard()

# Set up key bindings
screen.listen()
screen.onkey(rightPaddle.goUp, "Up")
screen.onkey(rightPaddle.goDown, "Down")
screen.onkey(leftPaddle.goUp, "w")
screen.onkey(leftPaddle.goDown, "s")

gameIsOn = True
while gameIsOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # Detect collision with walls and paddles
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    if (ball.distance(rightPaddle) < 50 and ball.xcor() > 320) or (ball.distance(leftPaddle) < 50 and ball.xcor() < -320):
        ball.bounceX()

    # Detect missed ball and update score
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreBoard.lScore()
    elif ball.xcor() < -380:
        ball.resetPosition()
        scoreBoard.rScore()

screen.exitonclick()
```

### paddle.py
Defines the Paddle class, which represents the player's paddle.
- Paddle Shape and Positioning: Each paddle is created as a white rectangle, with adjustable x/y coordinates.
- Movement: The goUp and goDown methods move the paddle vertically in response to player input.
```python
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def goUp(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def goDown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
```

### ball.py
Defines the Ball class, which handles the ball's movement and bouncing behavior.
- Ball Initialization: Creates a white circular ball that starts at the center.
- Ball Movement: Moves diagonally across the screen, bouncing off the walls and paddles
- Bounce and Speed Control: The bounceY and bounceX methods reverse direction upon collision, with bounceX also increasing speed each time it hits a paddle.
- Reset Position: The resetPosition method returns the ball to the center when a point is scored.
```python
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.1

    def move(self):
        new_x = self.xcor() + self.xMove
        new_y = self.ycor() + self.yMove
        self.goto(new_x, new_y)

    def bounceY(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1
        self.moveSpeed *= 0.9

    def resetPosition(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.bounceX()
```

### scoreboard.py
Defines the ScoreBoard class, which tracks and displays the players' scores.
- Score Initialization: Starts each player’s score at zero and displays it at the top of the screen.
- Score Update: Updates the score display each time a player scores.
```python
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lScore, align="center", font=("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(self.rScore, align="center", font=("Courier", 60, "bold"))

    def lScore(self):
        self.lScore += 1
        self.updateScoreBoard()

    def rScore(self):
        self.rScore += 1
        self.updateScoreBoard()
```

## ⚙️ Requirements
- Python 3.x
- Turtle graphics library (included with Python)

## ▶️ How to Run
1. Clone the repository or download the script files.
2. Run main.py to start the game:
```bash
python main.py
```
3. Use the arrow keys (Up, Down) to control the right paddle and W/S keys to control the left paddle.

## 📄 License
This project is open-source and available under the MIT License.



Enjoy a classic game of Pong with a modern twist! 🏓✨

