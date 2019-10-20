from manimlib.imports import *
import math
import numpy as np


class CobbDouglas(GraphScene):
        CONFIG = {
    "x_min": 0,
    "x_max": 5,
    "x_axis_width": 9,
    "x_tick_frequency": 1,
    "x_leftmost_tick": None, # Change if different from x_min
    "x_labeled_nums": None,
    "x_axis_label": "$x_1$",
    "y_min": 0,
    "y_max": 5,
    "y_axis_height": 6,
    "y_tick_frequency": 1,
    "y_bottom_tick": None, # Change if different from y_min
    "y_labeled_nums": None,
    "y_axis_label": "$x_2$",
    "axes_color": BLUE,
    "graph_origin": 2.5 * DOWN + 4 * LEFT,
    "exclude_zero_label": True,
    "num_graph_anchor_points": 25,
    "default_graph_colors": [BLUE, GREEN, YELLOW],
    "default_derivative_color": GREEN,
    "default_input_color": YELLOW,
    "default_riemann_start_color": BLUE,
    "default_riemann_end_color": GREEN,
    "area_opacity": 0.8,
    "num_rects": 50,
}

        def construct(self):
            self.setup_axes(animate=True)
            #Funktionen
            cobbdouglas = self.get_graph(self.cobbd,color=RED,x_min=0.01)
            constraint = self.get_graph(self.constraint)
            cobbdouglas2 = self.get_graph(self.cobbd2,color=ORANGE,x_min=0.01)
            constraint2 = self.get_graph(self.constraint2,x_max=5/2)
            PKK =self.get_graph(self.PKK)
            #TEXT
            intro=TextMobject("Cobb-Douglas Optimization")
            intro.shift(3*RIGHT)
            text = TextMobject("$d(p_1,p_2,Y)$ = $(\\frac{c}{c+d} \\frac{Y}{p_1},\\frac{d}{c+d} \\frac{Y}{p_2}$)")
            text.shift(3*RIGHT)
            text2 = TextMobject("$d(p_1^{\prime},p_2,Y)$ = $(\\frac{c}{c+d} \\frac{Y}{p_1^{\prime}},\\frac{d}{c+d} \\frac{Y}{p_2}$)")
            text2.shift(3*RIGHT)
            text3 = TextMobject("$p_1$ increases to $p_1^{\prime}$")
            text3.shift(3*RIGHT)
            text4 = TextMobject("$x_2^{\\ast}$ remains constant")
            text4.shift(3*RIGHT + UP)




            vert_line = self.get_vertical_line_to_graph(5/2,cobbdouglas,color=YELLOW)
            x = self.coords_to_point(0,5/4)
            y = self.coords_to_point(5/2,5/4)
            horz_line = Line(x,y,color=YELLOW)

            dottedline = DashedVMobject(horz_line)
            dottedlinevert = DashedVMobject(vert_line)
            point = Dot(self.coords_to_point(5/2,5/4))

            #lines for cobbdouglas2
            vert_line2 = self.get_vertical_line_to_graph(5/4,cobbdouglas2,color=YELLOW)
            x2 = self.coords_to_point(0,5/4)
            y2 = self.coords_to_point(5/4,5/4)
            horz_line2 = Line(x2,y2,color=YELLOW)
            dotted2vert = DashedVMobject(vert_line2)
            dotted2horz = DashedVMobject(horz_line2)
            point2 = Dot(self.coords_to_point(5/4,5/4))

            x3 = self.coords_to_point(5/4,5/4)
            y3 = self.coords_to_point(5/2,5/4)
            lineee= Line(x3,y3,color=YELLOW)
            dotted3 = DashedVMobject(lineee)

            #Animation
            self.play(Write(intro))
            self.play(ShowCreation(cobbdouglas))
            self.play(ShowCreation(cobbdouglas2))
            self.play(ShowCreation(constraint))
            self.play(ShowCreation(dottedline))
            self.play(ShowCreation(dottedlinevert))
            self.play(Write(point))
            self.play(FadeOut(intro))
            self.play(Write(text))
            self.wait(4)
            self.play(ReplacementTransform(text,text3))
            self.play(Transform(constraint,constraint2))
            self.play(FadeOut(dottedline))
            self.play(FadeOut(dottedlinevert))
            self.play(FadeOut(point))
            self.play(ShowCreation(dotted2vert))
            self.play(ShowCreation(dotted2horz))
            self.play(ShowCreation(dotted3))
            self.play(Write(point2))
            self.play(Transform(text3,text2))
            self.play(Write(text4))
            self.play(ShowCreation(PKK))
            self.wait()


        #Funktionen

        def PKK(self,Y):
            p1 = 0.5
            d = 2
            c = 2
            return(c/(c+d)*(Y/p1))


        def cobbd(self,x):
            return(9.765625**(1/2)/x) #c=2 and d=2 p1=1 p2=2

        def constraint(self,x):
            return((5-1*x)/2)

        def cobbd2(self,x):
            return(2.44140625**(1/2)/x) #p1=2 p2=2 x1=5/4 x2=5/4 c=2 d=2

        def constraint2(self,x):
            return((5-2*x)/2)
