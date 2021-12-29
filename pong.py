from tkinter import *
import random,time
tk=Tk()
tk.resizable(0,0)
tk.title("Pong")
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=500,bd=0)
canvas.config(bg="black")
canvas.pack()
tk.update()
canvas.create_line(250,0,250,500,fill="white")

class Ball:
    def __init__(self,canvas,color,paddle1,paddle2):
        self.canvas=canvas
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,215,250)
        starts=[-2,2]
        random.shuffle(starts)
        self.x =starts[0]
        self.y =-2

    def hit_paddle1(self,pos):
        paddle_pos=self.canvas.coords(self.paddle1.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                return True
            return False
    def hit_paddle2(self,pos):
        paddle_pos=self.canvas.coords(self.paddle2.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[2]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
                return True
            return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1] <=0:
            self.y=2
        if pos[3]>=500:
            self.y=-2
        if pos[0]<=0:
            self.x=2
        if pos[2]>=500:
            self.x=-2
        if self.hit_paddle1(pos)==True:
            self.x=2
        if self.hit_paddle2(pos)==True:
            self.x=-2
    def score(self,val):
        global counter1
        global counter2


class Paddle1:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,20,250,fill=color)
        self.y=0
        self.canvas.bind_all('q',self.turn_up)
        self.canvas.bind_all('a',self.turn_down)
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=500:
            self.y=0

    def turn_up(self, evt):
        self.y = -2

    def turn_down(self, evt):
        self.y = 2
class Paddle2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(480,150,500,250,fill=color)
        self.y=0
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=500:
            self.y=0

    def turn_up(self, evt):
        self.y = -2

    def turn_down(self, evt):
        self.y = 2

paddle1=Paddle1(canvas,"blue")
paddle2=Paddle2(canvas,"green")
ball=Ball(canvas,"red",paddle1,paddle2)

while 1:
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()