import turtle
import random
import math

R = 50
PHI = 360 / 7

# calculates radian
def phi_rad(i):
    phi_rad = PHI * i * math.pi / 180.0
    return phi_rad

# moves pen to mentioned coordinates
def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# draws circle with mentioned radius and filling color
def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

# draws gun barrel and foresight
def draw_barrel(x, y):
    turtle.speed(0)
    gotoxy(x, y)
    turtle.circle(80)
    gotoxy(x, y + 160)
    draw_circle(5, 'red')

    for i in range(0, 7):
        phi_rad(i)
        gotoxy(math.sin(phi_rad(i)) * R, math.cos(phi_rad(i)) * R + 60)
        draw_circle(20, 'white')

# turns barrel and checks if lose
def turn_barrel():
    start = 0

    for i in range(start, random.randrange(7, 70)):
        gotoxy(math.sin(phi_rad(i)) * R, math.cos(phi_rad(i)) * R + 60)
        draw_circle(20, 'brown')
        draw_circle(20, 'white')

    gotoxy(math.sin(phi_rad(i)) * R, math.cos(phi_rad(i)) * R + 60)
    draw_circle(20, 'brown')

    start = i % 7
    if start == 0:
        gotoxy(-150, 200)
        turtle.write('Вы проиграли!', font=('Arial', 18, 'normal'))


def main():
    draw_barrel(0, 0)
    answer = ''
    while answer.upper() != 'N':
        answer = turtle.textinput('Играть?', 'Y/N')

        if answer.upper() == 'Y':
            turn_barrel()

        else:
            pass


if __name__ == '__main__':
    main()