from manim import *

class SineWave(Scene):
    def construct(self):
        # Create a number plane
        plane = NumberPlane(x_range=[-4, 4], y_range=[-2, 2], axis_config={"color": BLUE})
        self.add(plane)
        
        # Create the sine wave
        sine_wave = always_redraw(lambda: plane.plot(lambda x: np.sin(x), color=YELLOW))

        # Create the labels for the axes
        x_label = MathTex("x").next_to(plane.x_axis, RIGHT)
        y_label = MathTex("f(x) = \sin(x)").next_to(plane.y_axis, UP)
        
        # Add the sine wave and labels to the scene
        self.play(Create(plane), Write(x_label), Write(y_label))
        self.play(Create(sine_wave), run_time=2)
        
        # Animate the sine wave
        self.play(sine_wave.animate.shift(RIGHT * 2), run_time=2)
        self.wait()

