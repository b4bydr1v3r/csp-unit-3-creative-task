from cmu_graphics import *

# GLOBAL VARIABLES
app.speed = 3
app.score = 0
app.colors = ['red', 'orange', 'yellow', 'lime']  # GLOBAL LIST

# GROUP
circles = Group()

def createCircles():
    spacing = 80  # LOCAL
    for i in range(len(app.colors)):  # TRAVERSE LIST
        color = app.colors[i]  # LOCAL
        circle = Circle(50 + i * spacing, 50, 20, fill=color)
        circles.add(circle)

def updateCircles():
    fallAmount = app.speed  # LOCAL
    for circle in circles.children:  # TRAVERSE GROUP CHILDREN
        circle.centerY += fallAmount
        if circle.centerY > 400:  # SELECTION
            circle.centerY = 0
            app.score += 1

def onStep():
    circles.centerX += 1  # GROUP PROPERTY
    updateCircles()

def onMousePress(x, y):
    clickedCount = 0  # LOCAL
    for circle in circles.children:  # TRAVERSE GROUP CHILDREN
        if circle.hits(x, y):  # SELECTION
            circle.fill = 'cyan'
            clickedCount += 1
    print('You clicked', clickedCount, 'circle(s)!')

createCircles()











cmu_graphics.run()