import random
import turtle as t

snake = t.Turtle()
t.bgcolor('white')

snake.shape("square")
snake.color("red")
snake.speed(0)
snake.penup()
snake.hideturtle()

food = t.Turtle()
food_form = ((0, 0), (14, 2), (18, 6), (20, 20), \
             (6, 18), (2, 14))
t.register_shape('food', food_form)
food.shape('square')
food.color('black')
food.penup()
food.hideturtle()
food.speed(0)

startatSpel = False
text = t.Turtle()
text.write('mellanslag = start yes', \
         align='center', font=('Arial', 16, 'bold'))
text.hideturtle()
text.color('black')

pointText = t.Turtle()
pointText.hideturtle()
pointText.speed(0)

def gameStart():
    global startatSpel
    if startatSpel:
        return
    startatSpel = True
    points = 0
    text.clear();

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
            snake_length = snake_length + 1
            snake.shapesize(1, snake_length, 1)
            snake_speed = snake_speed + 1
            points = points + 10
            showPoints(points)
        if outsideWindow():
            gameEnd()
            break

def moveUp():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def moveDown():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def moveLeft():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def moveRight():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

def gameEnd():
    snake.color('white')
    food.color('white')
    t.penup()
    t.hideturtle()
    t.write('lol du dog. kanske för att du har radeon', align='center', font=('Arial', 30, 'normal'))

def showPoints(actualPoints):
    pointText.clear()
    pointText.penup()
    x = (t.window_width() / 2) - 60
    y = (t.window_height() / 2) - 60
    pointText.setpos(x, y)
    pointText.write(str(actualPoints), align='right', font=('Arial', 40, 'bold'))

def placeFood():
    food.ht()
    food.setx(random.randint(-200, 200))
    food.sety(random.randint(-200, 200))
    food.st()

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

t.onkey(gameStart, 'space')
t.onkey(moveUp, 'w')
t.onkey(moveRight, 'd')
t.onkey(moveDown, 's')
t.onkey(moveLeft, 'a')
t.listen()
t.mainloop()