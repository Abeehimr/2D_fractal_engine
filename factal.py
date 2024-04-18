from settings import *

class Tree_Fractal:
    def __init__(self,app,maxlvl,branches,dO,dl,length) -> None:
        self.app = app
        
        self.maxlvl = maxlvl
        self.branches = branches
        self.dO = dO*(math.pi/180)
        self.dl = dl

        self.length = length

        self.q = deque([])
        

    def draw_whole(self):
        self.q = deque([])
        pos = INIT_POS
        def d(pos,lvl,leng, O_l , O_r):
            if lvl == self.maxlvl: return
            x,y = pos
            nl = self.dl*leng
            l = x+leng*math.sin(O_l) , y-leng*math.cos(O_l)
            r = x+leng*math.sin(O_r) , y-leng*math.cos(O_r)

            self.q.append((pos,l,"red"))#self.app.draw_line(pos,l,"red")

            d(l,lvl+1,nl,O_l-self.dO , O_l+self.dO)

            self.q.append((pos,r,"green"))#self.app.draw_line(pos,r,"green")

            d(r,lvl+1,nl,O_r-self.dO , O_r+self.dO)

        d(pos,0,self.length,0,0)

    def finish(self):
        while self.q:
            self.draw_branch()
        self.app.flip()

    def draw_branch(self):
        self.app.draw_line(*self.q.popleft())

    def draw_lvl(self):
        ...

    def update(self):
        if self.app.ani_trigger and self.q:
            self.draw_branch()
            self.app.flip()
    
