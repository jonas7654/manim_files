from manimlib.imports import *

class Text3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)

       

        self.add(axes)
        self.begin_ambient_camera_rotation()

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(ShowCreation(sphere))
        self.wait(2)
