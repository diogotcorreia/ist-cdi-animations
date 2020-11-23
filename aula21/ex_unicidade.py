from manim import *
import numpy as np
from math import floor


class EstudoFuncao(GraphScene):
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

        orig_func = self.get_graph(lambda x: np.cos(x), color=RED)
        origLab = self.get_graph_label(orig_func, label="f", direction=DOWN)

        self.play(ShowCreation(orig_func), ShowCreation(origLab))

        func_graph = self.get_graph(lambda x: np.sin(x), color=BLUE)
        fLab = self.get_graph_label(func_graph, label="F", direction=UP)

        self.play(ShowCreation(func_graph), ShowCreation(fLab))

        for i in range(-8, 8):
            splitFunc = self.get_graph(lambda x: self.funcSplit(
                x), x_min=i, x_max=i+0.9, color=GREEN)

            self.play(ShowCreation(splitFunc))
            if i == 7:
                fSplitLab = self.get_graph_label(splitFunc, label="F_2")
                self.play(ShowCreation(fSplitLab))

        self.wait(1)

    def funcSplit(self, x):
        k = floor(x)
        return np.sin(x) + k
