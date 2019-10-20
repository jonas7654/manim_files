from manimlib.imports import *
import math
import numpy as np

class PKK(GraphScene):
        CONFIG = {
    "x_min": 0,
    "x_max": 5.1,
    "x_axis_width": 9,
    "x_tick_frequency": 1,
    "x_leftmost_tick": None, # Change if different from x_min
    "x_labeled_nums": None,
    "x_axis_label": "$x_1$",
    "y_min": 0,
    "y_max": 5.1,
    "y_axis_height": 6,
    "y_tick_frequency": 1,
    "y_bottom_tick": None, # Change if different from y_min
    "y_labeled_nums": None,
    "y_axis_label": "$x_2$",
    "axes_color": BLUE,
    "graph_origin": 2.5 * DOWN + 4 * LEFT,
    "exclude_zero_label": True,
    "num_graph_anchor_points": 25,
    "default_graph_colors": [GREEN],
    "default_derivative_color": GREEN,
    "default_input_color": YELLOW,
    "default_riemann_start_color": BLUE,
    "default_riemann_end_color": GREEN,
    "area_opacity": 0.8,
    "num_rects": 50,
}



        def construct(self):
            self.setup_axes(animate=True)

            cobb = self.get_graph(self.cobbd,x_min=0.1)
            cobb2 = self.get_graph(self.cobbd2,x_min=0.1)
            cobb3 = self.get_graph(self.cobbd3,x_min=0.1)
            cobb4 = self.get_graph(self.cobbd4,x_min=0.1)
            cobb5 = self.get_graph(self.cobbd5,x_min=0.1)
            test= VGroup(cobb,cobb2,cobb3,cobb4,cobb5)
            PKKx1 = self.get_graph(self.PKK1,color=WHITE)
            c = self.get_graph(self.c1,color=RED)
            c2 = self.get_graph(self.c2,color=RED)
            c3 = self.get_graph(self.c3,color=RED)
            c4 = self.get_graph(self.c4,color=RED)
            c5 = self.get_graph(self.c5,color=RED)



            vertical = self.get_vertical_line_to_graph(2.5,cobb3,color=WHITE)


            self.play(ShowCreation(test))
            self.play(ShowCreation(PKKx1))
            self.play(ShowCreation(c))
            self.play(ShowCreation(c2))
            self.play(ShowCreation(c3))
            self.play(ShowCreation(c4))
            self.play(ShowCreation(c5))
            self.wait(4)







        def PKK1(self,p1):
            c=0.6
            d=0.4
            y=5
            return((d/(c+d))*y/1)


        def c1(self,x):
            y=5
            c=0.60
            d=0.4
            p1=1
            p2=1
            return((y-p1*x)/p2)

        def c2(self,x):
            y=5
            c=0.6
            d=0.4
            p1=2
            p2=1
            return((y-p1*x)/p2)

        def c3(self,x):
            y=5
            c=0.6
            d=0.4
            p1=3
            p2=1
            return((y-p1*x)/p2)

        def c4(self,x):
            y=5
            c=0.6
            d=0.4
            p1=4
            p2=1
            return((y-p1*x)/p2)

        def c5(self,x):
            y=5
            c=0.6
            d=0.4
            p1=5
            p2=1
            return((y-p1*x)/p2)


        def cobbd(self,x):
            y=5
            c=0.6
            d=0.4
            p1=1
            p2=1
            x1 = (c/(c+d))*y/p1
            x2 = (d/(c+d))*y/p2
            U = (x1**(c))*(x2**d)
            return((U/(x**c))**(1/d))

        def cobbd2(self,x):
            y=5
            c=0.6
            d=0.4
            p1=2
            p2=1
            x1 = (c/(c+d))*y/p1
            x2 = (d/(c+d))*y/p2
            U = (x1**(c))*(x2**d)
            return((U/(x**c))**(1/d))

        def cobbd3(self,x):
            y=5
            c=0.6
            d=0.4
            p1=3
            p2=1
            x>0
            x1 = (c/(c+d))*y/p1
            x2 = (d/(c+d))*y/p2
            U = (x1**(c))*(x2**d)
            return((U/(x**c))**(1/d))

        def cobbd4(self,x):
            y=5
            c=0.6
            d=0.4
            p1=4
            p2=1
            x>0
            x1 = (c/(c+d))*y/p1
            x2 = (d/(c+d))*y/p2
            U = (x1**(c))*(x2**d)
            return((U/(x**c))**(1/d))

        def cobbd5(self,x):
            y=5
            c=0.60
            d=0.4
            p1=5
            p2=1
            x1 = (c/(c+d))*y/p1
            x2 = (d/(c+d))*y/p2
            U = (x1**(c))*(x2**d)
            return((U/(x**c))**(1/d))
