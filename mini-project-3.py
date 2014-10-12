# template for "Stopwatch: The Game"

# Author: Ryanish

import simplegui

# define global variables

# main timer
main_timer = 0
# records successful watch stop
successful_stop = 0
# records the total number of stop button presses
total_stops = 0
# makes sure we can continue to keep recording total and successful stops and not mix us up with the 'main_timer' global variable
last_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(main_timer):
    A = main_timer // 600
    B = main_timer % 600 // 100
    C = main_timer % 100 // 10 
    D = main_timer % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global main_timer, successful_stop, total_stops, last_stop
    timer.stop()
    if last_stop != main_timer:
        total_stops = total_stops + 1
        if main_timer % 10 == 0:
            successful_stop = successful_stop + 1
        last_stop = main_timer

def reset():
    global main_timer, total_stops, last_stop
    timer.stop()
    main_timer = 0
    total_stops = 0
    successful_stop = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global main_timer
    main_timer = main_timer + 1
    
# define draw handler - this shows the objects in the canvas frame
def draw_stop_watch(canvas):
    canvas.draw_text(format(main_timer), (65, 50), 52, '#fff')
    canvas.draw_text(str(successful_stop) + " / " + str(total_stops), (95, 120), 40, '#ff0000')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 250, 175)
frame.set_canvas_background('Black')
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.start()

#register draw handler
frame.set_draw_handler(draw_stop_watch)

# register event handlers - the '100' digit is very important for displaying the correct equation on the watch
timer = simplegui.create_timer(100, timer_handler)


# start frame
frame.start()