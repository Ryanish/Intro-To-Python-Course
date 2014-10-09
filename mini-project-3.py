# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0

success_stop = 0
total_stop = 0
last_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t // 600
    B = t % 600 // 100
    C = t % 100 // 10 
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global t
    timer.start()
    
def stop():
    global t
    timer.stop()

def reset():
    global t
    timer.stop()
    t = 0

# define event handler for timer with 0.1 sec interval - DONE
def timer_handler():
    global t
    t = t + 1
    
# define draw handler
def draw_stop_watch(canvas):
    canvas.draw_text(format(t), (80, 50), 20, 'Red')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 250, 175)
frame.set_canvas_background('Black')
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.start()

#register draw handler
frame.set_draw_handler(draw_stop_watch)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)


# start frame
frame.start()