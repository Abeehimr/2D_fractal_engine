from settings import *
from factal import Tree_Fractal
from triangle import Triangle_Fractal
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('FRACTALS')
        self.screen = pg.display.set_mode(WIN)
        self.clock = pg.time.Clock()
        #self.tree_fractal = Tree_Fractal(self,15,2,0,0.75,150)
        # self.tree_fractal.draw_whole()
        self.tri_fractal = Triangle_Fractal(self,7)
        self.tri_fractal.draw_whole()
        self.set_timer()

    def draw_background(self):
        self.screen.fill(color=FIELD_COLOR)
        self.flip()

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.ani_trigger = False
        pg.time.set_timer(self.user_event,TICK)

    def update(self):
        #self.tree_fractal.update()
        self.tri_fractal.update()
        self.clock.tick(FPS)
        
    def draw(self):
        self.draw_background()
        # if self.ani_trigger: #and self.tree_fractal.dO <= math.pi/2:
        #     self.loop()
        #     self.flip()


    def draw_line(self,i_pos , f_pos,color):
        pg.draw.line(self.screen,color,i_pos,f_pos)

    def flip(self):
        pg.display.flip()


    def check_events(self):
        self.ani_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.tri_fractal.finish()
                #     self.tree_fractal.finish()
            if event.type == self.user_event:
                self.ani_trigger = True

    def loop(self):
        # self.tree_fractal.draw_whole()
        # self.tree_fractal.finish()
        # self.tree_fractal.dO += math.pi/180
        self.tri_fractal.test()


    def run(self):
        self.draw_background()
        while True:
            self.check_events()
            self.update()
            #self.draw()

            

if __name__ == '__main__':
    app = App()
    app.run()