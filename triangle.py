from settings import *

class Triangle_Fractal:
    def __init__(self,app,maxdepth) -> None:
        self.app = app
        self.maxdepth = maxdepth
        self.A = vec(WIN_W//2,0)
        half = math.tan(math.pi/6)*(WIN_H-1)
        self.B , self.C = vec(WIN_W//2-half , WIN_H-1) , vec(WIN_W//2+half , WIN_H-1)

        

    def draw_whole(self):

        self.q = deque([(self.A,self.B,self.C,"green")])
        pos = INIT_POS
        def d(lvl,a,b,c,color):
            if lvl == self.maxdepth or a == b  or a == c or b == c: return
            ab ,ac , bc = (a+b)//2 , (a+c)//2 , (b+c)//2
            self.q.append((ab,ac,bc,color))
            ncolor = "red" if color == "green" else "green"
            d(lvl+1,a,ab,ac,ncolor)
            d(lvl+1,ab,b,bc,ncolor)
            d(lvl+1,ac,bc,c,ncolor)
        d(0,self.A,self.B,self.C,"red")

    def finish(self):
        while self.q:
            self.draw_triangle(*self.q.popleft())
        self.app.flip()

    def draw_next(self):
        self.draw_triangle(*self.q.popleft())

    def draw_lvl(self):
        ...

    def update(self):
        if self.app.ani_trigger and self.q:
            self.draw_next()
            self.app.flip()

    def draw_triangle(self,a,b,c,color):
        self.app.draw_line(a,b,color)
        self.app.draw_line(a,c,color)
        self.app.draw_line(b,c,color)

