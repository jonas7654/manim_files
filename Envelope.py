from manimlib.imports import *
import numpy as np
import time

class Envelope(GraphScene):
        CONFIG = {
    "x_min": -20,
    "x_max": 20,
    "x_axis_width": 9,
    "x_tick_frequency": 50,
    "x_leftmost_tick": None, # Change if different from x_min
    "x_labeled_nums": None,
    "x_axis_label": "$x$",
    "y_min": -50,
    "y_max": 50,
    "y_axis_height": 9,
    "y_tick_frequency": 50,
    "y_bottom_tick": None, # Change if different from y_min
    "y_labeled_nums": None,
    "deriv" : [lambda x: -b**2+x*b+2 for b in range(10)], # [lambda x: 2*x*i-i**2 for i in range(8)]
    "y_axis_label": "$y$",
    "axes_color": WHITE,
    "graph_origin": ORIGIN + 2*DOWN,
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
            self.setup_axes(animate=False)
            
            valuefunc = self.get_graph(self.Valuefunction)
            envtheorem_Text = TextMobject("Envelope Theorem")
            envtheorem_Text.shift(3*UP)
            Intro_text = TexMobject("V(a) = \\frac{1}{4}a^2")
            eq1 = TexMobject("\\frac{d}{da}f(x^{\\ast}(a);a)", #0
                             "=",  #1
                             "\\sum{\\frac{\partial f}{\partial x_i}(x^{\\ast}(a);a)", #2
                             "\\cdot", #3
                             "\\frac{dx_i^{\\ast}(a)}{da}}", #4
                             "+" , #5
                             "\\frac{\partial f}{\partial a}(x^{\\ast}(a);a)" #6
                             )
            eq1_brace = Brace(eq1[2])
            texteq1brace = eq1_brace.get_text("$= 0$")
            example = TextMobject("Example")
            example.shift(2*UP)
            exampleEQ = TexMobject("f(x;a) = -x^2 + ax") #V(a) = \\frac{1}{4}a^2
            eq = TexMobject("f(x;a) = -x^2 + ax \ \\implies \ V(a) = \\frac{1}{4}a^2")
            
            self.play(FadeOut(self.axes))
            self.play(FadeIn(envtheorem_Text))
            self.play(Write(eq1),run_time = 2.5)
            self.wait(3)
            self.play(GrowFromCenter(eq1_brace),GrowFromCenter(texteq1brace))
            self.wait(2)
            self.play(FadeOut(eq1_brace),FadeOut(texteq1brace),FadeOut(eq1[2]),FadeOut(eq1[3]),FadeOut(eq1[4]),FadeOut(eq1[5]))
            self.wait()
            self.play(ApplyMethod(eq1[6].shift,eq1[1].get_corner(LEFT) + 2.96*LEFT),run_time = 2)
            self.play(ApplyMethod(eq1[0].shift,3*RIGHT),ApplyMethod(eq1[1].shift,3*RIGHT),ApplyMethod(eq1[6].shift,3*RIGHT))
            self.wait(3.5)
            self.play(FadeOut(eq1[0]),FadeOut(eq1[1]),FadeOut(eq1[6]))
            self.wait(2)
            self.play(ShowCreation(valuefunc))
            self.wait(3)

            for b in np.arange(-5,5,0.1):
                envelope2 = lambda x: -b**2+x*b+2
                envelope_manim = self.get_graph(envelope2,color = YELLOW)
                self.play(ShowCreation(envelope_manim),run_time = 0.2)
            
            self.wait(5)




        def Valuefunction(self,x):
            return((1/4)*x**2 + 2)

        