import turtle
import ball
import random


class Simulation:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.ball_list = []


        for i in range(num_balls):
            x = random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius)
            y = random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius)
            vx = 10*random.uniform(-1.0, 1.0)
            vy = 10*random.uniform(-1.0, 1.0)
            ball_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            self.ball_list.append(ball.Ball(ball_color, self.ball_radius, x, y, vx, vy))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def run(self):
        dt = 0.2  # time step
        while True:
            turtle.clear()
            self.draw_border()
            for i in range(self.num_balls):
                self.ball_list[i].draw()
                self.ball_list[i].move(dt)
                self.ball_list[i].update_velocity()
            turtle.update()


simulation = Simulation(num_balls=5)
simulation.run()

