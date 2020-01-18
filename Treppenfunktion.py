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

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 2,
        "y_min": -1,
        "y_max": 6,
        "graph_origin": ORIGIN+2.5*DOWN,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-1, 3, 1),
        # "x_labeled_nums": [-1, -0.5, 0, 0.5, 1],
        # "x_labeled_nums": [(-1, -1), (-0.5, -0.5), (0, 0), (0.5, 0.5), (1,1)],
        "y_labeled_nums": range(0, 8, 2),
        # "num_rects": 1000,
        # "num_graph_anchor_points": 6000,
        # "discontinuities": [0,1],
    }

    def construct(self):

        def func_to_graph(self, x):
            if x > 0:
                return 1 / x
            else:
                return 0

        def func_to_graph2(self, x):
            n = self.n
            if x > 0:
                sum = 0
                # A_1 =
                # A_2 =
                if x * n < 1:
                    sum += n
                for k in range(0, n * (2 ** n)):
                    B_1 = k / (2 ** n)
                    B_2 = (k + 1) / (2 ** n)
                    if B_1 * x < 1 <= B_2 * x:
                        sum += k / (2 ** n)
                return sum
            else:
                return 0

        self.setup_axes(animate=True)
        # self.x_axis_labels = [-1, -0.5, 0, 0.5, 1]
        max = 5
        graphs = []
        for n in range(1,max + 1):
            self.n = n

            func_graph2 = VGroup()
            wurzel = lambda x: func_to_graph(self, x)
            treppe = lambda x: func_to_graph2(self, x)

            if n < 7:
                j = 1 / n

                graph = self.get_graph(treppe, YELLOW, x_min=0.0000001, x_max=j - 0.0001)
                func_graph2.add(graph)

            i = n * (2 ** n) - 1
            while (0 <= i <= n * (2 ** n) - 1) and ((2 ** n) / i < 2):
                j = i / (2 ** n)
                k = (i + 1) / (2 ** n)
                j = 1 / j  # -0.1
                k = 1 / k
                k_y = func_to_graph2(self, k)
                j_y = func_to_graph2(self, j)
                if (j-k) < 0.005 and False:
                    graph = self.get_graph(wurzel, YELLOW, x_min=k, x_max=j)
                else:
                    if (j-k) < 0.01:
                        j = j - (j - k) / 100
                    else:
                        j = j - (j - k) / 100
                    graph = self.get_graph(treppe, YELLOW, x_min=k, x_max=j)
                func_graph2.add(graph)
                i -= 1
            k = (i + 1) / (2 ** n)
            j = 2
            k = 1 / k
            graph = self.get_graph(treppe, YELLOW, x_min=k, x_max=j - 0.0000001)
            func_graph2.add(graph)
            graphs.append(func_graph2)

        for n in range(1,max + 1):
            self.n = n
           

            func_graph = self.get_graph(self.func_to_graph, self.function_color, x_min=1 / 6)
            vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
            graph_lab = self.get_graph_label(func_graph, label="\\frac{1}{x}", direction=2 * UP)
            two_pi = TexMobject("x = 2 \\pi")
            label_coord = self.input_to_graph_point(TAU, func_graph)
            two_pi.next_to(label_coord, RIGHT + UP)
            if n==1:
                self.play(ShowCreation(func_graph), ShowCreation(graphs[n-1]))
            else:
                self.play(Transform(graphs[0], graphs[n-1]))
            self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(two_pi))
            self.wait(2)

    def func_to_graph(self, x):
        if x > 0:
            return 1 / x
        else:
            return 0
