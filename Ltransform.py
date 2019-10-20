from manimlib.imports import *
import math
import numpy as np

class LinearTransformation(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "foreground_plane_kwargs": {
            "color": GREY,
            "axis_config": {
            "stroke_color": RED,
            "x_max": 10,
            }


        },
        "background_plane_kwargs": {
            "color": GREY,
            "axis_config": {
                "stroke_color": PURPLE,
                "x_max": FRAME_WIDTH / 2,
                "x_min": -FRAME_WIDTH / 2,
                "y_max": FRAME_WIDTH / 2,
                "y_min": -FRAME_WIDTH / 2,
            },
            "number_line_config": {
                "color": GREY,
                "x_max": 10,

            },
            "background_line_style": {
                "stroke_color": GREY,
                "stroke_width": 1,

            },
        },
        "show_coordinates": True,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 6,
        "i_hat_color": X_COLOR,
        "j_hat_color": Y_COLOR,
        "leave_ghost_vectors": False,
        "t_matrix": [[3, 0], [1, 2]],
    }

    def construct(self):
        matrix = [[2, -2], [3 , 3]]
        v = [1, 2]
        b = [1, 9]
        c = TextMobject("$Vector \ Transformation$")





        self.add_title(c)
        self.wait(2)
        self.play(FadeOut(c))
        self.add_vector(v)
        self.apply_matrix(matrix)
        self.apply_inverse(matrix)
        self.wait()
