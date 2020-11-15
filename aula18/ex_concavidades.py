from manim import *
import numpy as np

class ExemploConcavidades(GraphScene):
    CONFIG = {
        "x_axis_visibility": True,
        "x_min": 0,
        "x_max": 6,
        "x_label_position": RIGHT,
        "y_axis_visibility": True,
        "y_min": 0,
        "y_max": 20,
        "y_axis_config": {"tick_frequency": 5},
        "axes_color" : WHITE,
    }

    def construct(self):
        self.setup_axes()
        dot = Dot().move_to(self.coords_to_point(1, 0))
        func_graph = self.get_graph(lambda x: self.f(x), color=BLUE, min=0)

        derivative = self.get_derivative_graph(func_graph, COLOR=GREEN)
        secondD = self.get_derivative_graph(derivative, color=RED)
        thirdD = self.get_derivative_graph(secondD, color=YELLOW)
        
        fLab = self.get_graph_label(func_graph, label="f", direction=LEFT)
        f1Lab = self.get_graph_label(derivative, label="f'")
        f2Lab= self.get_graph_label(secondD, label="f''", x_val=1)
        f3Lab = self.get_graph_label(thirdD, label="f^{(3)}")

        fExp = MathTex(r'f(x)=4x^3-3x^2-6x^2\log x+3x', color=BLUE).scale(0.7)
        fExp.to_corner(RIGHT+UP)
        f1Exp = MathTex(r"f'(x)=12x^2-6x-12x\log x -6x+3", color=GREEN).scale(0.6)
        f1Exp.to_corner(RIGHT+UP)
        f2Exp = MathTex(r"f''(x)=24x-24-12\log x", color=RED).scale(0.7)
        f2Exp.to_corner(RIGHT+UP)
        f3Exp = MathTex(r"f^{(3)}(x)=24-\frac{12}x", color=YELLOW)
        f3Exp.to_corner(RIGHT+UP)

        desc = MathTex(r"f^{(3)}(1)=12 \ne 0\\\text{Logo, }f(1) \text{ é ponto de inflexão}").scale(0.7)
        desc.to_corner(RIGHT+UP)

        self.play(ShowCreation(fExp), ShowCreation(func_graph), ShowCreation(fLab))
        self.wait(2)
        self.play(Transform(fExp, f1Exp), ShowCreation(derivative), ShowCreation(f1Lab))
        self.wait(2)
        self.play(Transform(fExp, f2Exp), ShowCreation(secondD), ShowCreation(f2Lab), ShowCreation(dot))
        self.wait(2)
        self.play(Transform(fExp, f3Exp), ShowCreation(thirdD), ShowCreation(f3Lab))
        self.wait(1)
        self.play(Transform(fExp, desc))
        
        self.wait(5)

    def f(self, x):
      if x<= 0:
        return 0
      return 4*(x**3)-3*(x**2)-6*(x**2)*np.log(x)+3*x