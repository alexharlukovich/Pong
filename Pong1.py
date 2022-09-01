from tkinter import *
import random

# global variables. They will be useful for easier customize our's game's window

# window settings

WIDTH = 1000
HEIGHT = 350

# racket settings

PAD_W = 10
PAD_H = 100

#add global variables for the racket's moving speed
PAD_SPEED = 20

#speed for the left platform
LEFT_PAD_SPEED = 0

#speed for the right platform
RIGHT_PAD_SPEED = 0

# ball settings
BALL_RADIUS = 30

#add global variables for the ball's speed
#by horizontal
BALL_X_CHANGE = 20
#by vertical
BALL_Y_CHANGE = 0

#how much will increases the ball's speed after each hit
BALL_SPEED_UP = 1.05
#maximum ball's speed
BALL_MAX_SPEED = 40
#initial horizontal velocity
BALL_X_SPEED = 20
#initial vertical velocity
BALL_Y_SPEED = 20
#add a global variable responsible for the distance
#to the right edge of the playing field
right_line_distance= WIDTH - PAD_W
#add global variables player's scores
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

#add a global variable INITIAL_SPEED
INITIAL_SPEED = 20


# set the window
root = Tk()
root.title("White_Rabbit's Pong")

# animation area
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

# elements of the playing field

# left line
c.create_line(PAD_W,0, PAD_W, HEIGHT, fill="white")

# right line
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="white")


# central line
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="red")

# set the ball
BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+BALL_RADIUS/2, fill="white")

# set the left racket
LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="yellow")

# set the right racket
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, PAD_H, width=PAD_W, fill="yellow")

#add text objects which will display the player's score
p_1_text = c.create_text(WIDTH - WIDTH / 6, PAD_H / 4,
                         text=PLAYER_1_SCORE,
                         font="Arial 20",
                         fill="white")

p_2_text = c.create_text(WIDTH / 6, PAD_H / 4,
                         text=PLAYER_2_SCORE,
                         font="Arial 20",
                         fill="white")



#create move_ball function for ball moving

def move_ball():
#determinate the ball's coordinates and its center
    ball_left, ball_right, ball_top, ball_bot = c.coords(BALL)
    ball_center = ( ball_top + ball_bot ) / 2
#vertical bounce
#if we are far from vertical lines- just moving the ball
    if ball_right + BALL_X_SPEED < right_line_distance and ball_left + BALL_X_SPEED > PAD_W:
       c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
    # If the ball touches its right or left side of the field boundary
    elif ball_right == right_line_distance or ball_left == PAD_W:
# Check the right or left side we touch
        if ball_right > WIDTH / 2:
# If right, then compare the position of the center of the ball
# with the position of the right racket
# And if the ball is within the racket, we make a rebound
            if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
                bounce("strike")
            else:
                update_score("left")
                spawn_ball()
        else:
            if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
                bounce("strike")
            else:
                update_score("right")
                spawn_ball()
# Checking the situation in which the ball can fly out of the boundaries of the playing field.
# In this case, just move it to the border of the field.
    else:
        if ball_right > WIDTH / 2:
            c.move(BALL, right_line_distance - ball_right, BALL_Y_SPEED)
        else:
            c.move(BALL, -ball_left+PAD_W, BALL_Y_SPEED)
#horisontal bounce
    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("ricochet")

# create a main function in which we will call move_ball and recursively ourselves through root.after

def main():
    move_ball()
    move_pads()
    root.after(30, main)

#function for moving both of pads

def move_pads():
# for convenience, let's create a dictionary where the racket corresponds to its speed
    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}
    #sorting through the rackets
    for pad in PADS:
        # move the racket at a given speed
        c.move(pad, 0, PADS[pad])
        # if the racket gets out of the playing field, we return it to its place
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])
# set focus on Canvas to responds on keystrokes

c.focus_set()

#function for processing keystrokes

def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED == -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED == PAD_SPEED

#bind this function to Canvas

c.bind("<KeyPress>", movement_handler)

#create function to respond releasing keys

def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0

#bind this function to Canvas

c.bind("<KeyRelease>", stop_pad)

#ball bounce function

def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED
#hit ball with a racket
    if action == "strike":
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
        BALL_Y_SPEED = -BALL_Y_SPEED


# create function for changing the score and respawn the ball

def update_score(player):
    global PLAYER_1_SCORE,PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)

def spawn_ball():
    global BALL_X_SPEED
    # set ball on center
    c.coords(BALL, WIDTH/2-BALL_RADIUS/2,
             HEIGHT/2-BALL_RADIUS/2,
             WIDTH/2+BALL_RADIUS/2,
             HEIGHT/2+BALL_RADIUS/2)
# Set the direction of the ball towards the losing player,
# but reduce the speed to the original
BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)


# start window run
main() #!!!!

root.mainloop()

