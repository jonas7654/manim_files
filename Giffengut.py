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

            #Define Funktions for Animation
            u1 = self.get_graph(self.u1,color=WHITE,x_min=4.01,x_max=6.5)
            u2 = self.get_graph(self.u2,color=WHITE,x_min=4.01,x_max=7.3)
            u3 = self.get_graph(self.u3,color=WHITE,x_min=4.01,x_max=8.5)
            u4 = self.get_graph(self.u4,color=WHITE,x_min=4.01,x_max=10.2)
            u5 = self.get_graph(self.u5,color=WHITE,x_min=4.01,x_max=13.35)
            u6 = self.get_graph(self.u6,color=WHITE,x_min=4.01,x_max=14)
            u7 = self.get_graph(self.u7,color=WHITE,x_min=4.01,x_max=14)
            ind = VGroup(u1,u2,u3,u4,u5,u6,u7)
            constraint = self.get_graph(self.constraint,color=RED)
            constraint2 = self.get_graph(self.constraint2,color=RED)
            constraint3 = self.get_graph(self.constraint3,color=RED)
            constraint4 = self.get_graph(self.constraint4,color=RED)
            constraint5 = self.get_graph(self.constraint5,color=RED)
            constraint6 = self.get_graph(self.constraint6,color=RED)
            constraint7 = self.get_graph(self.constraint7,color=RED)



            #TextMobject
            GiffenFunc = TextMobject("$U=\\frac{x_1-4}{(6-x_2)^2}$")
            GiffenFunc.scale(0.95)
            GiffenFunc.shift(UP)
            #
            GiffenFuncforTransform = TextMobject("$U=\\frac{x_1-4}{(6-x_2)^2}$")
            GiffenFuncforTransform.shift(UP)
            GiffenFuncforTransform.scale(0.95)
            #
            Text1 = TextMobject("Giffen Good")
            Text1.to_edge(UP)
            #
            Text2 = TextMobject("The Indifference Curves \\linebreak are given by $g(x_1)$")
            Text2.scale(0.8)
            #
            Text3 = TextMobject("Our Optimal Bundle is given by \\linebreak \\linebreak $d(p_1,p_2,Y)$ = $(\\frac{8p1+6p2-Y}{p1},-\\frac{8p1-6p2+2Y}{p2})$")
            Text3.scale(0.9)
            Text3.shift(UP)
            #
            ContourLine = TextMobject("$g(x_1)=6-\\frac{\\sqrt{(x_1-4)}}{U}$")
            ContourLine.shift(Text2.get_corner(DOWN)+0.65*DOWN)
            ContourLine.scale(0.95)
            #
            Intro = TextMobject("Our Utility is given by")
            Intro.scale(0.95)
            Intro.shift(2*UP)

            #FADEOUT SECTION
            constraintGROUP = VGroup(constraint,constraint3,constraint4,constraint5,constraint6,constraint7)
            ufade = VGroup(u1,u3,u4,u5,u6)
            ufade2 = VGroup(u2,u3,u4,u5,u6,u7)
            fade = VGroup(constraintGROUP,ufade)
            TextFade = VGroup(Intro,Text2)



            #
            # u1text = TextMobject("$U_1$")
            # u1text.scale(0.4)
            # u1text.next_to(u1)
            # u1text.shift(0.6*DOWN+2*LEFT)



            #ANIMATION
            self.play(Write(Text1))
            self.play(Write(Intro))
            self.play(Write(GiffenFunc))
            self.wait(1)
            self.play(Write(Text2))
            self.wait(1)
            self.play(Transform(GiffenFuncforTransform,ContourLine),run_time=1.5)
            self.wait(1.5)
            self.play(FadeOut(TextFade))
            #self.play(ApplyMethod(GiffenFuncforTransform.scale,0.65))
            self.play(ApplyMethod(GiffenFunc.to_edge,0.5*LEFT))
            self.play(ApplyMethod(GiffenFuncforTransform.shift,Intro.get_corner(DOWN)+1.75*UP))
            self.play(ShowCreation(ind),run_time=2)
            self.wait()
            self.play(FadeOut(ufade2))
            self.wait()
            self.play(Write(Text3))
            # self.play(ShowCreation(constraint))
            # self.play(ShowCreation(constraint2))
            # self.play(ShowCreation(constraint3))
            # self.play(ShowCreation(constraint4))
            # self.play(ShowCreation(constraint5))
            # self.play(ShowCreation(constraint6))
            # self.play(ShowCreation(constraint7))
            # self.wait()
            # self.play(FadeOut(fade))
            # self.wait()





# FUNCTIONS
        def constraint(self,x):
            p1=1.2
            p2=1
            Y = 8
            return((Y-p1*x)/p2)

        def constraint2(self,x):
            p1=1.1
            p2=1
            Y = 8
            return((Y-p1*x)/p2)

        def constraint3(self,x):
            p1=1
            p2=1
            Y = 8
            return((Y-p1*x)/p2)

        def constraint4(self,x):
            p1=0.9
            p2=1
            Y = 8
            return((Y-p1*x)/p2)

        def constraint5(self,x):
            p1=0.8
            p2=1
            Y = 8
            return((Y-p1*x)/p2)

        def constraint6(self,x):
            p1=0.7
            p2=1
            Y = 8
            return((Y-p1*x)/p2)

        def constraint7(self,x):
            p1=0.6
            p2=1
            Y = 8
            return((Y-p1*x)/p2)


        def u1(self,x):
            p1=1.2
            p2=1
            Y = 8
            x1=(8*p1+6*p2-Y)/p1
            x2=(-8*p1-6*p2+2*Y)/p2
            u = (x1-4)/(6-x2)**2
            return(6-((x-4)/u)**(1/2))

        def u2(self,x):
            p1=1.1
            p2=1
            Y = 8
            x1=(8*p1+6*p2-Y)/p1
            x2=(-8*p1-6*p2+2*Y)/p2
            u = (x1-4)/(6-x2)**2
            return(6-((x-4)/u)**(1/2))

        def u3(self,x):
            p1=1
            p2=1
            Y = 8
            x1=(8*p1+6*p2-Y)/p1
            x2=(-8*p1-6*p2+2*Y)/p2
            u = (x1-4)/(6-x2)**2
            return(6-((x-4)/u)**(1/2))

        def u4(self,x):
            p1=0.9
            p2=1
            Y = 8
            x1=(8*p1+6*p2-Y)/p1
            x2=(-8*p1-6*p2+2*Y)/p2
            u = (x1-4)/(6-x2)**2
            return(6-((x-4)/u)**(1/2))

        def u5(self,x):
            p1=0.8
            p2=1
            Y = 8
            x1=(8*p1+6*p2-Y)/p1
            x2=(-8*p1-6*p2+2*Y)/p2
            u = (x1-4)/(6-x2)**2
            return(6-((x-4)/u)**(1/2))

        def u6(self,x):
            p1=0.7
            p2=1
            Y = 8
            x1=(8*p1+6*p2-Y)/p1
            x2=(-8*p1-6*p2+2*Y)/p2
            u = (x1-4)/(6-x2)**2
            return(6-((x-4)/u)**(1/2))

        def u7(self,x):
            p1=0.6
            p2=1
            Y = 8
            x1=(8*p1+6*p2-Y)/p1
            x2=(-8*p1-6*p2+2*Y)/p2
            u = (x1-4)/(6-x2)**2
            return(6-((x-4)/u)**(1/2))
