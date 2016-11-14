import tkinter

WIDTH = 840
HEIGHT = 650
BG_COLOR = 'white'
ZERO = 0


class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
        
        
    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                       fill=self.color)
                       
                       
    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.y, self.y  + self.r, fill=BG_COLOR, outline=BG_COLOR)
        
        
    def move(self):
        if(self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= ZERO):
            self.dx = -self.dx
        if(self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERO):
            self.dy = - self.dy
        self.x += self.dx
        self.y += self.dy
        self.draw()


def mouse_click(events):
    global main_ball
    if events.num == 1:
        main_ball = Balls(events.x, events.y, 25, 'green', 5, 5)
        main_ball.draw()
        main_ball.move()
    else:
        main_ball.hide()
        
        
def movement():
    if 'main_ball' in globals():
        main_ball.move()
    root.after(10, movement)
    


root = tkinter.Tk()
root.title("Driving")
canvas = tkinter.Canvas(root, width=WIDTH,height=HEIGHT,bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-3>',mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
movement()
root.mainloop()