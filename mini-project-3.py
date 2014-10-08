# template for "Stopwatch: The Game"

import simplegui

# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


#timer.is.running()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    pass
# define draw handler

    
# create frame
frame = simplegui.create_frame("Stopwatch", 250, 175)
frame.set_canvas_background('Black')
frame.start()

# register event handlers
timer = simplegui.create_timer(500, timer_handler)


# start frame

timer.start()
timer.stop()

# Please remember to review the grading rubric
"""
1 pt - The program successfully opens a frame with the stopwatch stopped.
1 pt - The program has a working "Start" button that starts the timer.
1 pt - The program has a working "Stop" button that stops the timer.
1 pt - The program has a working "Reset" button that stops the timer (if running) and resets the timer to 0.
"""


