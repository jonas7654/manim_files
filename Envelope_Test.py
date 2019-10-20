from manimlib.imports import *
import math
import numpy as np

class Giffen(GraphScene):
        CONFIG = {
    "x_min": 0,
    "x_max": 15,
    "x_axis_width": 9,
    "x_tick_frequency": 1,
    "x_leftmost_tick": None, # Change if different from x_min
    "x_labeled_nums": None,
    "x_axis_label": "$x_1$",
    "y_min": 0,
    "y_max": 15,
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

            u1 = self.get_graph(self.u1,color=WHITE,x_min=4.01,x_max=14)
            constraint = self.get_graph(self.constraint,color=RED)
            constraint2 = self.get_graph(self.constraint2,color=RED)
            constraint3 = self.get_graph(self.constraint3,color=RED)
            constraint4 = self.get_graph(self.constraint4,color=RED)
            constraint5 = self.get_graph(self.constraint5,color=RED)
            constraint6 = self.get_graph(self.constraint6,color=RED)
            constraint7 = self.get_graph(self.constraint7,color=RED)
            c8 = self.get_graph(self.constraint8,color=RED)
            c9 = self.get_graph(self.constraint9,color=RED)
            c10 = self.get_graph(self.constraint10,color=RED)
            c11 = self.get_graph(self.constraint11,color=RED)
            c12 = self.get_graph(self.constraint12,color=RED)
            c13 = self.get_graph(self.constraint13,color=RED)
            c14 = self.get_graph(self.constraint14,color=RED)
            c15 = self.get_graph(self.constraint15,color=RED)
            c16 = self.get_graph(self.constraint16,color=RED)

            envelope = VGroup(constraint,constraint2,constraint3,constraint4,constraint5,constraint6,
                              constraint7,c8,c9,c10,c11,c12,c13,c14,c15,c16)


            self.play(ShowCreation(u1))
            self.play(ShowCreation(envelope),run_time=10)


        def constraint(self,x):
            p1=0.5
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint2(self,x):
            p1=0.4
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint3(self,x):
            p1=0.1
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint4(self,x):
            p1=1
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint5(self,x):
            p1=1.25
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint6(self,x):
            p1=1.2
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint7(self,x):
            p1=1.1
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint8(self,x):
            p1=0.3
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint9(self,x):
            p1=0.4
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint10(self,x):
            p1=0.35
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint11(self,x):
            p1=0.25
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint12(self,x):
            p1=0.2
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint13(self,x):
            p1=0.15
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint14(self,x):
            p1=0.1
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint15(self,x):
            p1=0.5
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)

        def constraint16(self,x):
            p1=0.25
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            return((Y-p1*x)/p2)


        def u1(self,x):
            p1=10
            p2=1
            Y = (32*p1**2+48*p1*p2-p2**2)/(8*p1)
            x1=(8*p1+6*p2-Y)/p1
            x2=(-8*p1-6*p2+2*Y)/p2
            u = (x1-4)/(6-x2)**2
            return(6-((x-4)/u)**(1/2))
