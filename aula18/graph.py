from manim import *
import numpy as np

class FunctionPlotWithLabbeledYAxe(GraphScene):
    CONFIG = {
        "graph_origin" : ORIGIN,
        "x_min": -1,
        "x_max": 1,
        "y_min": -5,
        "y_max": 5,
    }

    def construct(self):
        self.setup_axes()
        a = 2
        dot = Dot().move_to(self.coords_to_point(0, 0))
        func_graph = self.get_graph(lambda x: np.sinh(a * x))

        polinomial = self.get_graph(lambda x: self.pol(a,x))

        remainder = self.get_graph(lambda x: self.rest(a,x))

        #sumFunc = self.get_graph(lambda x: self.pol(a,x)+self.rest(a,x), color=RED)

        graph_lab = self.get_graph_label(func_graph, label="\\sinh(ax)")
        polinomial_lab = self.get_graph_label(polinomial, label="P_4(x)",x_val=-1.2, direction=DOWN / 2)
        remainder_lab = self.get_graph_label(remainder, label="R_4(x)")


        self.play(ShowCreation(func_graph), ShowCreation(graph_lab), ShowCreation(dot))
        self.play(ShowCreation(polinomial), ShowCreation(polinomial_lab))
        self.play(ShowCreation(remainder), ShowCreation(remainder_lab))
        #self.play(ShowCreation(sumFunc))
        
        self.wait(5)
        ##self.play(FadeOut(func_graph))

    def pol (self, a, x):
        return a*x+((a*x)**3)/6

    def rest (self, a,x):
        return (a**5)*np.cosh(a*(x-0.01))*(x**5)/120