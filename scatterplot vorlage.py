from manimlib.imports import *
import math

class CSV(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 100,
        "x_axis_width": 6,
        "x_tick_frequency": 10,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 10,
        "y_axis_height": 6,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$y$",
        "axes_color": BLUE,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
    }


    def construct(self):
        self.setup_axes()
        coords = self.return_coords_from_csv("data")
        dots = VGroup(*[Dot().move_to(self.coords_to_point(coord[0],coord[1])) for coord in coords])
        lm = self.get_graph(self.linear,color=RED)
        self.play(ShowCreation(dots))
        self.play(ShowCreation(lm),run_time=3)

    def return_coords_from_csv(self,file_name):
        import csv
        coords = []
        with open(f'/Users/jonas/Desktop/TEST20.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                x,y = row
                coord = [float(x),float(y)]
                coords.append(coord)
        csvFile.close()
        return coords

    def linear(self,x):
        return(0.07912*x+2.71927)
