from manim import *
import numpy as np


class FuncaoAssintotas1(GraphScene):
    CONFIG = {
        "x_axis_visibility": True,
        "x_min": -8,
        "x_max": 8,
        "y_axis_visibility": True,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "axes_color": WHITE,
    }

    def construct(self):
        self.setup_axes()
        func_graph1 = self.get_graph(
            lambda x: self.func(x), x_min=-8, x_max=-0.1, color=BLUE)
        func_graph2 = self.get_graph(
            lambda x: self.func(x), x_min=0.1, x_max=8, color=BLUE)

        self.play(ShowCreation(func_graph1))
        self.play(ShowCreation(func_graph2))

        self.wait(1)

    def func(self, x):
        return 1/x


class FuncaoAssintotas2(GraphScene):
    CONFIG = {
        "x_axis_visibility": True,
        "x_min": -8,
        "x_max": 8,
        "y_axis_visibility": True,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "axes_color": WHITE,
    }

    def construct(self):
        self.setup_axes()
        func_graph1 = self.get_graph(
            lambda x: self.func(x), x_min=-8, x_max=-0.1, color=BLUE)
        func_graph2 = self.get_graph(
            lambda x: self.func(x), x_min=0.2, x_max=8, color=BLUE)

        self.play(ShowCreation(func_graph1))
        self.play(ShowCreation(func_graph2))

        self.wait(1)

    def func(self, x):
        if (x == 0):
            return 0
        return np.exp(1/x)
