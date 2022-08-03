import random
import turtle as t

# Set fullscren
screen = t.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

# Background Color and Title
t.bgcolor('white')
t.title("Snake on a Budget")

# Snake Turtle
snake = t.Turtle()
snake.shape("square")
snake.color("red")
snake.speed(0)
snake.penup()
snake.hideturtle()

# Food Turtle
food = t.Turtle()
food_form = ((0, 0), (14, 2), (18, 6), (20, 20), \
             (6, 18), (2, 14))
t.register_shape('food', food_form)
food.shape('square')
food.color('black')
food.penup()
food.hideturtle()
food.speed(0)

# Is game started?
startatSpel = False

# Text to show instructions
text = t.Turtle()
text.write('Press space to start the game', \
         align='center', font=('Arial', 60, 'bold'))
text.hideturtle()
text.color('black')

# Text to show credits
creditsText = t.Turtle()
creditsText.write('Made by @VenixDeveloper; Contribution from @Gampisen', align='center', font=('Arial', 10, 'normal'))
creditsText.hideturtle()
creditsText.color('black')

# Point text
pointText = t.Turtle()
pointText.hideturtle()
pointText.speed(0)

# Calls to start game
def gameStart():
    global startatSpel
    if startatSpel:
        return
    startatSpel = True
    points = 0
    text.clear();
    creditsText.clear();

    snake_speed = 2
    snake_length = 3
    snake.shapesize(1, snake_length, 1)
    snake.showturtle()
    showPoints(points)
    placeFood()

    while True:
        snake.forward(snake_speed)
        if snake.distance(food) < 20:
            placeFood()
            snake_length += 1
            snake.shapesize(1, snake_length, 1)
            snake_speed += 1
            points += 1
            showPoints(points)
        if outsideWindow():
            gameEnd()
            break
# Move up
def moveUp():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

# Move down
def moveDown():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

# Move left
def moveLeft():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

# Move right
def moveRight():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

# Calls to end game
def gameEnd():
    snake.color('white')
    food.color('white')
    t.penup()
    t.hideturtle()
    t.write('You died.', align='center', font=('Arial', 30, 'normal'))
    startatSpel = False

# Calls to show points
def showPoints(actualPoints):
    pointText.clear()
    pointText.penup()
    x = (t.window_width() / 2) - 20
    y = (t.window_height() / 2) - 40
    pointText.setpos(x, y)
    pointText.write('Your current points: ' + str(actualPoints), align='right', font=('Arial', 20, 'normal'))

# Calls when food needs to be spawned
def placeFood():
    food.ht()
    food.setx(random.randint(-200, 200))
    food.sety(random.randint(-200, 200))
    food.st()

# Calls when snake is outside of the window
def outsideWindow():
    leftWindow = -t.window_width() / 2
    rightWindow = t.window_width() / 2
    topWindow = t.window_height() / 2
    bottomWindow = -t.window_height() / 2
    (x, y) = snake.pos()
    outside = \
            x< leftWindow or \
            x> rightWindow or \
            y< bottomWindow or \
            y> topWindow
    return outside

# On Key
t.onkey(gameStart, 'space')
t.onkey(moveUp, 'w')
t.onkey(moveRight, 'd')
t.onkey(moveDown, 's')
t.onkey(moveLeft, 'a')

# Turtle wants some attention.
t.listen()
t.mainloop()