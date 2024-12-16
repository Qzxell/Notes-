from manim import *

class ParametricEquation(Scene):
    def construct(self):
        # Create a number plane
        plane = NumberPlane(x_range=[0, 13], y_range=[0, 13], axis_config={"color": BLUE})
        self.add(plane)

        # Define the parametric equation
        parametric_curve = ParametricFunction(
            lambda t: np.array([
                t + np.sin(5 * t),
                t + np.sin(5 * t),
                0
            ]),
            t_range=np.array([0, 13]),
            color=YELLOW
        )

        # Add the parametric curve to the scene
        self.play(Create(plane), Create(parametric_curve), run_time=4)
        self.wait()
