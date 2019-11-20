#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

# For manim-version of May-15-19
class PlotDashed(GraphScene):
    CONFIG = {
        "y_max" : 5,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : 0,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : BLUE,
        "x_label_decimal":1,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal":1
    }
    y=2
    def construct(self):
        self.setup_axes(animate=False)
        graph = self.get_graph(lambda x : x,
                                    color = GREEN,
                                    )
        graph2 = self.get_graph(lambda x : -x+5, color=RED,x_max=5)
        dashed_graph=DashedVMobject(graph)

        vert=self.get_vertical_line_to_graph(2.5,graph,color=YELLOW)
        vertD=DashedVMobject(vert)

        x=Line(1,2)

        self.play(Write(graph2))
        self.play(Write(graph))
        self.play(Write(vertD),run_time=2)
        self.play(Write(x))

        self.wait()

class Graphing(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 5,
        "y_min": 0,
        "y_max": 5,
        "y_tick_frequency":1,
        "x_tick_frequency":1,
        "graph_origin": 5 * LEFT + 3* DOWN,
        "function_color": WHITE,
        "axes_color": BLUE,
        "x_axis_label": "$q$",
        "y_axis_label": "$p$"
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,color=RED,x_min=0.01)
        graph_lab = self.get_graph_label(func_graph, label = "D(p)")

        func_graph_2=self.get_graph(self.func_to_graph_2,color=YELLOW)
        graph_lab3  = self.get_graph_label(func_graph_2,label="GK=P")
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "S(p)")
        EQ = TexMobject("D(p)=S(p)",color=YELLOW)

        vert_line = self.get_vertical_line_to_graph(1.310370697,func_graph,color=WHITE)

        x = self.coords_to_point(0,2.289428485)
        y = self.coords_to_point(1.310370697,2.289428485)
        horz_line = Line(x,y, color=WHITE)

        point = Dot(self.coords_to_point(1.3103,2.289),color=WHITE)
        dashed_graph=DashedVMobject(horz_line)
        dashed_graph2=DashedVMobject(vert_line)

        #test=self.input_to_graph_point(2,func_graph)



        self.play(ShowCreation(func_graph_2))
        self.play(Write(graph_lab3))
        self.play(ShowCreation(func_graph))
        self.play(Write(graph_lab))
        self.play(Transform(graph_lab3,graph_lab_2))
        self.play(Write(EQ))
        self.wait(1)
        self.play(ShowCreation(dashed_graph2))
        self.play(ShowCreation(dashed_graph))
        self.play(Write(point))
        #self.play(ShowCreation(test))
        self.wait(3)
        #self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        #self.wait(2)


    def func_to_graph(self, x):
        return (3/x)

    def func_to_graph_2(self,x):
        return(2*x**(1/2))
