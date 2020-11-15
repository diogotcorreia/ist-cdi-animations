from manim import *
import numpy as np

class FunctionPlotWithLabbeledYAxe(GraphScene):
    CONFIG = {
        "x_axis_visibility": True,
        "x_min": -10,
        "x_max": 10,
        "x_label_position": RIGHT,
        "y_axis_visibility": True,
        "y_min": -50,
        "y_max": 50,
        "y_label_position": UP,
        "y_axis_config": {"tick_frequency": 10},
        "y_labeled_nums": np.arange(-50, 50, 10),
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : WHITE,
        "include_tip" : True,
    }

    def construct(self):
        self.setup_axes()
        dot = Dot().move_to(self.coords_to_point(PI / 2, 20))
        func_graph = self.get_graph(lambda x: 20 * np.sin(x))

        derivative = self.get_derivative_graph(func_graph)

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(dot))
        self.play(ShowCreation(derivative))
        
        self.wait(1)
        self.play(FadeOut(func_graph))