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
    "y_tick_frequency": 15,
    "y_bottom_tick": None, # Change if different from y_min
    "y_labeled_nums": None,
    "y_axis_label": "$x_2$",
    "axes_color": WHITE,
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
            u1 = self.get_graph(self.u1,color=YELLOW,x_min=4.01,x_max=6.5)
            u2 = self.get_graph(self.u2,color=YELLOW,x_min=4.01,x_max=7.2)
            u3 = self.get_graph(self.u3,color=YELLOW,x_min=4.01,x_max=8.5)
            u4 = self.get_graph(self.u4,color=YELLOW,x_min=4.01,x_max=10.2)
            u5 = self.get_graph(self.u5,color=YELLOW,x_min=4.01,x_max=13.35)
            u6 = self.get_graph(self.u6,color=YELLOW,x_min=4.01,x_max=14)
            u7 = self.get_graph(self.u7,color=YELLOW,x_min=4.01,x_max=14)
            constraint = self.get_graph(self.constraint,color=RED,x_max=6.8)
            constraint2 = self.get_graph(self.constraint2,color=RED)
            constraint3 = self.get_graph(self.constraint3,color=RED)
            constraint4 = self.get_graph(self.constraint4,color=RED)
            constraint5 = self.get_graph(self.constraint5,color=RED)
            constraint6 = self.get_graph(self.constraint6,color=RED)
            constraint7 = self.get_graph(self.constraint7,color=RED)



            #TextMobject
            GiffenFunc = TextMobject(("$U$=$\\frac{x_1-4}{(6-x_2)^2}$"),tex_to_color_map={"$U$": YELLOW})
            GiffenFunc.scale(0.95)
            GiffenFunc.shift(UP)
            #
            Eq = TextMobject("$ \Leftrightarrow $")
            Eq.next_to(GiffenFunc)
            Eq.scale(0.95)
            #
            GiffenFuncforTransform = TexMobject(("U = {x-4 \\over (6-g(x_1))^2}"),tex_to_color_map={"g(x_1)": YELLOW})
            GiffenFuncforTransform.next_to(Eq)
            GiffenFuncforTransform.scale(0.95)

            #
            GiffenFuncwithg = TexMobject(("U = {x-4 \\over (6-g(x_1))^2}"),tex_to_color_map={"g(x_1)": YELLOW})
            GiffenFuncwithg.scale(0.85)
            GiffenFuncwithg.next_to(Eq)
            #
            Text1 = TextMobject("Giffen good",color=WHITE)
            Text1.to_edge(UP)
            #
            Text2 = TextMobject(("The Indifference Curves \\linebreak are given by $g(x_1)$"),
                    tex_to_color_map={"$g(x_1)$": YELLOW}
                    )
            Text2.scale(0.8)
            #
            Text3 = TextMobject("$d(p_1,p_2,Y)=$",           #0
                                "$(\\frac{8p1+6p2-Y}{p1},-\\frac{8p1-6p2+2Y}{p2})$")
            Text3[0].set_color("66ff33")
            Text3.scale(0.85)
            Text3.shift(UP+0.5*RIGHT)
            #
            ContourLine = TextMobject(("$g(x_1)$=$6-\\sqrt{\\frac{(x_1-4)}{U}}$"),
                        tex_to_color_map={"$g(x_1)$": YELLOW}
                        )
            ContourLine.shift(Text2.get_corner(DOWN)+0.65*DOWN)
            ContourLine.scale(0.95)
            #
            Intro = TextMobject(("Our Utility is given by"),
                    tex_to_color_map={"Utility":YELLOW})
            Intro.scale(0.95)
            Intro.shift(2*UP)
            #
            Text4 = TextMobject("$d(p_1,p_2,Y)=$",           #0
                                "$(\\frac{8p1+6p2-Y}{p1}$,",    #1
                                "$-\\frac{8p1-6p2+2Y}{p2})$")  #2
            Text4[0].set_color("66ff33")
            Text4.scale(0.65)
            Text4.shift((Intro.get_corner(DOWN))+RIGHT+0.5*UP)
            braceforx1 = Brace(Text4[1],DOWN,buff = SMALL_BUFF)
            t1 = braceforx1.get_text("$x_1$")
            t1.scale(0.8)
            t1.shift(0.2*UP)
            braceforx1.shift(0.1*UP)


            braceforx2 = Brace(Text4[2],DOWN,buff = SMALL_BUFF)
            t2 = braceforx2.get_text("$x_2$")
            t2.scale(0.8)
            t2.shift(0.2*UP)
            braceforx2.shift(0.1*UP)

            parentfortext4 = VGroup(braceforx1,braceforx2)
            parenttext4 = VGroup(t1,t2)

            #
            Text5 = TextMobject("if $p_1$ decreases our Budgetline gets flatter")
            Text5.scale(0.85)
            Text5.shift(RIGHT+0.5*UP)
            #
            Text6 = TextMobject("$p_1$=$1.2$")
            Text6.shift(2*RIGHT+UP)
            #
            Text7 = TextMobject("$p_1$=$1.1$")
            Text7.shift(2*RIGHT+UP)
            #
            Text8 = TextMobject("$p_1$=$1$")
            Text8.shift(2*RIGHT+UP)
            #
            Text9 = TextMobject("$p_1$=$0.9$")
            Text9.shift(2*RIGHT+UP)
            #
            Text10 = TextMobject("$p_1$=$0.8$")
            Text10.shift(2*RIGHT+UP)
            #
            Text11 = TextMobject("$p_1$=$0.7$")
            Text11.shift(2*RIGHT+UP)
            #
            Text12 = TextMobject("$p_1$=$0.6$")
            Text12.shift(2*RIGHT+UP)
            #
            Text13 = TextMobject("Giffen good :"
                                 "if $p_1 \\uparrow$",               #0
                                 "$\Longrightarrow$",                #1
                                 "$x_1(\\ast) \\downarrow$")         #

            Text13.scale(0.85)
            Text13.shift(2*RIGHT+UP)
            #
            Text14 = TextMobject("$d(p_1,p_2,Y)=$", #0
                                "$(6.181818$,",     #1
                                "$1.2$)")            #2
            Text14.shift((Intro.get_corner(DOWN))+RIGHT+0.5*UP)
            Text14.scale(0.65)
            Text14[0].set_color("66ff33")


            #lines/dots
            vert_line1 = self.get_vertical_line_to_graph((8*1.2+6*1-8)/1.2,u1,color=WHITE)
            xu1 = self.coords_to_point(0,(-8*1.2-6*1+2*8)/1)
            yu1 = self.coords_to_point((8*1.2+6*1-8)/1.2,(-8*1.2-6*1+2*8)/1)
            horz_line1 = Line(xu1,yu1,color="WHITE")
            dottedlinehorz1 = DashedVMobject(horz_line1)
            dottedlinevert1 = DashedVMobject(vert_line1)
            dot1 = Dot(self.coords_to_point((8*1.2+6*1-8)/1.2,(-8*1.2-6*1+2*8)/1))
            dot1.set_color("66ff33")
            dot1.scale(0.5)
            line1group = VGroup(dottedlinehorz1,dottedlinevert1,dot1)
            #
            vert_line2 = self.get_vertical_line_to_graph((8*1.1+6*1-8)/1.1,u2,color=WHITE)
            xu2 = self.coords_to_point(0,(-8*1.1-6*1+2*8)/1)
            yu2 = self.coords_to_point((8*1.1+6*1-8)/1.1,(-8*1.1-6*1+2*8)/1)
            horz_line2 = Line(xu2,yu2,color="WHITE")
            dottedlinehorz2 = DashedVMobject(horz_line2)
            dottedlinevert2 = DashedVMobject(vert_line2)
            dot2 = Dot(self.coords_to_point((8*1.1+6*1-8)/1.1,(-8*1.1-6*1+2*8)/1))
            dot2.set_color("66ff33")
            dot2.scale(0.5)
            line2group = VGroup(dottedlinehorz2,dottedlinevert2,dot2)
            #
            vert_line3 = self.get_vertical_line_to_graph((8*1+6*1-8)/1,u3,color=WHITE)
            xu3 = self.coords_to_point(0,(-8*1-6*1+2*8)/1)
            yu3 = self.coords_to_point((8*1+6*1-8)/1,(-8*1-6*1+2*8)/1)
            horz_line3 = Line(xu3,yu3,color="WHITE")
            dottedlinehorz3 = DashedVMobject(horz_line3)
            dottedlinevert3 = DashedVMobject(vert_line3)
            dot3 = Dot(self.coords_to_point((8*1+6*1-8)/1,(-8*1-6*1+2*8)/1))
            dot3.set_color("66ff33")
            dot3.scale(0.5)
            line3group = VGroup(dottedlinehorz3,dottedlinevert3,dot3)
            #
            vert_line4 = self.get_vertical_line_to_graph((8*0.9+6*1-8)/0.9,u4,color=WHITE)
            xu4 = self.coords_to_point(0,(-8*0.9-6*1+2*8)/1)
            yu4 = self.coords_to_point((8*0.9+6*1-8)/0.9,(-8*0.9-6*1+2*8)/1)
            horz_line4 = Line(xu4,yu4,color="WHITE")
            dottedlinehorz4 = DashedVMobject(horz_line4)
            dottedlinevert4 = DashedVMobject(vert_line4)
            dot4 = Dot(self.coords_to_point((8*0.9+6*1-8)/0.9,(-8*0.9-6*1+2*8)/1))
            dot4.set_color("66ff33")
            dot4.scale(0.5)
            line4group = VGroup(dottedlinehorz4,dottedlinevert4,dot4)
            #
            vert_line5 = self.get_vertical_line_to_graph((8*0.8+6*1-8)/0.8,u5,color=WHITE)
            xu5 = self.coords_to_point(0,(-8*0.8-6*1+2*8)/1)
            yu5 = self.coords_to_point((8*0.8+6*1-8)/0.8,(-8*0.8-6*1+2*8)/1)
            horz_line5 = Line(xu5,yu5,color="WHITE")
            dottedlinehorz5 = DashedVMobject(horz_line5)
            dottedlinevert5 = DashedVMobject(vert_line5)
            dot5 = Dot(self.coords_to_point((8*0.8+6*1-8)/0.8,(-8*0.8-6*1+2*8)/1))
            dot5.set_color("66ff33")
            dot5.scale(0.5)
            line5group = VGroup(dottedlinehorz5,dottedlinevert5,dot5)
            #
            vert_line6 = self.get_vertical_line_to_graph((8*0.7+6*1-8)/0.7,u6,color=WHITE)
            xu6 = self.coords_to_point(0,(-8*0.7-6*1+2*8)/1)
            yu6 = self.coords_to_point((8*0.7+6*1-8)/0.7,(-8*0.7-6*1+2*8)/1)
            horz_line6 = Line(xu6,yu6,color="WHITE")
            dottedlinehorz6 = DashedVMobject(horz_line6)
            dottedlinevert6 = DashedVMobject(vert_line6)
            dot6 = Dot(self.coords_to_point((8*0.7+6*1-8)/0.7,(-8*0.7-6*1+2*8)/1))
            dot6.set_color("66ff33")
            dot6.scale(0.5)
            line6group = VGroup(dottedlinehorz6,dottedlinevert6,dot6)
            #
            vert_line7 = self.get_vertical_line_to_graph((8*0.6+6*1-8)/0.6,u7,color=WHITE)
            xu7 = self.coords_to_point(0,(-8*0.6-6*1+2*8)/1)
            yu7 = self.coords_to_point((8*0.6+6*1-8)/0.6,(-8*0.6-6*1+2*8)/1)
            horz_line7 = Line(xu7,yu7,color="WHITE")
            dottedlinehorz7 = DashedVMobject(horz_line7)
            dottedlinevert7 = DashedVMobject(vert_line7)
            dot7 = Dot(self.coords_to_point((8*0.6+6*1-8)/0.6,(-8*0.6-6*1+2*8)/1))
            dot7.set_color("66ff33")
            dot7.scale(0.5)
            line7group = VGroup(dottedlinehorz7,dottedlinevert7,dot7)

            #VGROUPS
            ind = VGroup(u1,u2,u3,u4,u5,u6,u7)
            constraintGROUP = VGroup(constraint,constraint3,constraint4,constraint5,constraint6,constraint7)
            ufade = VGroup(u1,u3,u4,u5,u6)
            ufade2 = VGroup(u2,u3,u4,u5,u6,u7)
            uinput = VGroup(u4,u5,u6,u7)
            fade = VGroup(constraintGROUP,ufade)
            TextFade = VGroup(Intro,Text2)
            EQU = VGroup(Eq,GiffenFuncwithg)
            LINEGROUPFORFADEOUT = VGroup(line1group,line2group,line3group,line4group,line5group,line6group,line7group)
            linedotucfade = VGroup(LINEGROUPFORFADEOUT,fade)



            #ANIMATION
            self.play(Write(Text1))
            self.play(Write(Intro))
            self.play(Write(GiffenFunc))
            self.wait(1)
            self.play(Write(Text2))
            self.play(Write(EQU))
            self.wait(1)
            self.play(Transform(GiffenFuncwithg,ContourLine),run_time=1.5)
            self.play(FadeOut(Eq))
            self.wait(1.5)
            self.play(FadeOut(TextFade))
            self.play(ApplyMethod(GiffenFunc.to_edge,0.5*LEFT))
            self.play(ApplyMethod(GiffenFuncwithg.shift,Intro.get_corner(DOWN)+1.75*UP))
            self.play(ShowCreation(ind),run_time=2)
            self.wait()
            self.play(FadeOut(ufade2))
            self.wait()
            self.play(Write(Text3))
            self.play(ShowCreation(constraint))
            self.play(ShowCreation(dottedlinehorz1))
            self.play(ShowCreation(dottedlinevert1))
            self.play(ShowCreation(dot1))
            self.wait()
            self.play(ApplyMethod(GiffenFuncwithg.scale,0.65))
            self.play(ApplyMethod((GiffenFuncwithg.move_to),(GiffenFunc.get_corner(DOWN))+DOWN))
            self.play(Transform(Text3,Text4))
            self.play(GrowFromCenter(parentfortext4),FadeIn(parenttext4))
            self.play(Write(Text5))
            self.wait(1.5)
            self.play(Transform(Text5,Text6))
            self.wait()
            self.play(Transform(Text5,Text7))
            self.play(ShowCreation(constraint2))
            self.play(FadeOut(parentfortext4),FadeOut(parenttext4))

            self.play(Transform(Text3,Text14))

            # self.play(ShowCreation(u2))
            # self.play(Write(line2group))
            # self.play(Transform(Text5,Text8))
            # self.play(ShowCreation(constraint3))
            # self.play(ShowCreation(u3))
            # self.play(Write(line3group))
            # self.play(ShowCreation(uinput))
            # self.play(Transform(Text5,Text9))
            # self.play(ShowCreation(constraint4))
            # self.play(ShowCreation(line4group))
            # self.play(Transform(Text5,Text10))
            # self.play(ShowCreation(constraint5))
            # self.play(ShowCreation(line5group))
            # self.play(Transform(Text5,Text11))
            # self.play(ShowCreation(constraint6))
            # self.play(ShowCreation(line6group))
            # self.play(Transform(Text5,Text12))
            # self.play(ShowCreation(constraint7))
            # self.play(ShowCreation(line7group))
            # self.wait()
            # self.play(FadeOut(linedotucfade))
            # self.play(Write(Text13))
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
