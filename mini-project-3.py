# template for "Stopwatch: The Game"

import simplegui

# define global variables
counter = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()

def reset():
    global counter
    counter = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    print counter
    counter += 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text("it needs to go here", (80, 50), 20, 'White')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 250, 175)
frame.set_canvas_background('Black')
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.start()

# register event handlers
timer = simplegui.create_timer(1000, timer_handler)


# start frame
"""
Write the event handler function for the canvas that 
draws the current time (simply as an integer, you
should not worry about formatting it yet) in the middle
of the canvas. Remember that you will need to convert the 
current time into a string using str before drawing it.
"""