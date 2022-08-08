import _tkinter as tk
from turtle import Screen, TurtleScreen
from time import sleep
import PySimpleGUI as sg
from snake import Snake
from food import Food
from scoreboard import Scoreboard as sb
from numpy import ceil

def game():

    def sleep_time_update(sleep_time): return sleep_time / 3

    def speed_update(speed): return int(ceil(speed*1.1))

    points = 0
    sleep_var = 0.018
    root = Screen()
    TurtleScreen._RUNNING = True
    root.setup(width=800, height=800)
    root.bgcolor("green")
    root.title("Snake")
    root.tracer(0)
    sn = Snake()
    f = Food()
    g = f.generate_food()
    root.listen()
    root.onkey(sn.left, key="Left")
    root.onkey(sn.right, key="Right")
    root.onkey(sn.up, key="Up")
    root.onkey(sn.down, key="Down")
    i_o = True
    speed = 5
    try:
        while i_o:
            root.update()
            sleep(sleep_var)
            sn.move(speed)

            if sn.head.distance(f) < 20:
                g = f.generate_food()
                sn.seg_adder()
                snake_len = len(sn.parts)-3 # -3 because we started with three pieces
                if snake_len % 50 == 0: sleep_var = sleep_time_update(sleep_var)
                if snake_len % 200 == 0: speed = speed_update(speed)
                points += 1
            if sn.head.xcor() > 399 or sn.head.ycor() > 399 or sn.head.xcor() < -399 or sn.head.ycor() < -399:
                root.bye()
                i_o = False
            for seg in sn.parts:  # have to use rangelen because I dont care about the first set of collisions that are guaranteed to touch the head
                if sn.parts.index(seg) > 10:  # buffer to prevent auto destruction
                    if sn.head.distance(seg) < 3:
                        root.bye()
                        i_o = False
                        break
    except tk.TclError:
        print("")
    try:
        root.bye()
    except Exception:
        pass
    return points

h = sb()
sg.theme('DarkTeal9')
gui_layout = [
    [
        sg.Button("Start Game"),
        sg.Button("End"),
        sg.Button("Show High Scores"),
    ],
    [
        sg.Text("The snake is controlled by the arrow keys and\n" +
                "gets faster as he gets longer. The end button\n" +
                "is the preferred way to stop the program.")
    ],
    [
        sg.Text("Username: "),
        sg.InputText(key="-USER_NAME-"),
    ],
    [
        sg.Output(expand_y=True),
    ]
]
start_menu = sg.Window(title="KCH39\'s Snek Game", size=(350, 600), layout=gui_layout, resizable=True)

while True:
    event, values = start_menu.read()

    if event == "End" or sg.WIN_CLOSED or sg.WINDOW_CLOSED:
        start_menu.close()
        break

    elif event == "Start Game":
        username = values.get("-USER_NAME-")
        s = game()
        user_score_list = [username, s]
        h.new_score(user_score_list)
        print("Game Over!\n" + username + " won " + str(s) + " points! Thanks for playing!")

    elif event == "Show High Scores":
        try:
            h = sb()
            print(h.show_top().head(15))
        except Exception:
            print(h.show_top())

    else:
        continue
