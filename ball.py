import turtle
import math


class Ball:
    def __init__(self, color, size, x, y, vx, vy):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]

    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def update_velocity(self):
        if abs(self.x) > self.canvas_width:
            self.vx = -self.vx

        if abs(self.y) > self.canvas_height:
            self.vy = -self.vy


