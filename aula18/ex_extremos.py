from manim import *
import numpy as np

class ExemploExtremos(GraphScene):
    CONFIG = {
        "x_axis_visibility": True,
        "x_min": -6,
        "x_max": 6,
        "x_label_position": RIGHT,
        "y_axis_visibility": True,
        "y_min": -20,
        "y_max": 20,
        "y_label_position": UP,
        "y_axis_config": {"tick_frequency": 5},
        "graph_origin" : ORIGIN ,
        "axes_color" : WHITE,
    }

    def construct(self):
        self.setup_axes()
        dot = Dot().move_to(self.coords_to_point(0, 0))
        func_graph = self.get_graph(lambda x: self.f(x))

        derivative = self.get_derivative_graph(func_graph)
        secondD = self.get_derivative_graph(derivative, color=RED)
        
        fLab = self.get_graph_label(func_graph, label="f")
        f1Lab = self.get_graph_label(derivative, label="f'", x_val=-6)
        f2Lab= self.get_graph_label(secondD, label="f''")

        fExp = MathTex(r'f(x)=e^{x\sin x}-2x^2', color=BLUE)
        fExp.to_corner(RIGHT+UP)
        f1Exp = MathTex(r"f'(x)=(\sin x+x\cos x)e^{x\sin x}-4x", color=GREEN).scale(0.8)
        f1Exp.to_corner(RIGHT+UP)
        f2Exp = MathTex(r"f''(x)=(2\cos x - x\sin x + (\sin x + x\cos x)^2) e^{x\sin x}-4", color=RED).scale(0.5)
        f2Exp.to_corner(RIGHT+UP)

        desc = MathTex(r"f''(0)=-2 < 0\\\text{Logo, }f(0) \text{ é máximo}")
        desc.to_corner(RIGHT+UP)

        self.play(ShowCreation(fExp), ShowCreation(func_graph), ShowCreation(fLab))
        self.wait(2)
        self.play(Transform(fExp, f1Exp), ShowCreation(derivative), ShowCreation(f1Lab), ShowCreation(dot))
        self.wait(2)
        self.play(Transform(fExp, f2Exp), ShowCreation(secondD), ShowCreation(f2Lab))
        self.wait(1)
        self.play(Transform(fExp, desc))
        
        self.wait(5)

    def f(self, x):
      return np.exp(x * np.sin(x))-2*(x**2)