import numpy as np
import math
from Tkinter import *
import keyboard
import Tkinter as tk

points = list()
file = open('point.poly', 'w')
file.truncate(0)

exit_flag = False
def close_file():
	global file, exit_flag
	print 'file closed'
	exit_flag = True
	file.close()
	win.destroy()

def initWorld(canvas, x, y):
	global file, win, exit_flag
	radius = 5.
	colors = ["white", "blue", "yellow", "#FAA"]
	canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = colors[1])
	print 'exit flag', exit_flag
	if x>= 0 and y>=0:
		file.write(str(round(x/78.,2))+' '+str(round(y/78.,2))+'\n')

def callback(event):
	point = [event.x * world_scale, event.y * world_scale]
	points.append(point)
	print "clicked at", event.x, event.y
	initWorld(canvas, event.x, event.y)
	


def motion(event):
	x, y = event.x, event.y
	print('{}, {}'.format(x, y))


pixelsize = 780
framedelay = 1
world_xmin = 0.
world_ymin = 0.
world_xmax = 10.
world_ymax = 10.
world_width = world_xmax - world_xmin
world_height = world_ymax - world_ymin
world_scale = pixelsize / world_width
win = Tk()
win.bind("<Button-1>", callback)
# win.bind('<Motion>', motion)

canvas = Canvas(win, width = pixelsize, height = pixelsize * world_height / world_width)
win.geometry("+{}+{}".format(2500, 100))
canvas.pack()
win.protocol("WM_DELETE_WINDOW", close_file)
win.after(framedelay, lambda: callback)
tk.mainloop()
