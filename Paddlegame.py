from tkinter import *
import random
import time

tk = Tk()
tk.title("Ball Paddle Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-a>', self.bob)
        self.canvas.bind_all('<KeyPress-d>', self.jim)
        self.canvas.bind_all('KeyPress-s>', self.joey)
        self.canvas.bind_all('KeyPress=w?', self.garen)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos [0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def bob(self, evt):
        self.x = -2
    def jim(self, evt):
        self.x = 2
    def joey(self, evt):
        self.y = 2
    def garen(self, evt):
        self.y = -2
        
    

ball = Ball(canvas, 'red')
paddle = Paddle(canvas, 'yellow')

while 1:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(.01)
    
    
