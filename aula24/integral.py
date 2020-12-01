from manim import *


class IntegralPlot(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 5,
        "x_tick_frequency": 1,
        "x_labeled_nums": [1, 3],
        "y_min": 0,
        "y_max": 4,
        "num_graph_anchor_points": 50,
    }

    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x: self.func(x), x_min=0, x_max=5)

        # self.revert_to_original_skipping_status()
        self.play(ShowCreation(graph))
        self.wait(1)

        side = "right"

        rect_list = self.get_riemann_rectangles_list(
            graph, 7,
            max_dx=0.5,
            x_min=1,
            x_max=3,
            input_sample_type=side
        )
        flat_graph = self.get_graph(lambda t: 0)
        rects = self.get_riemann_rectangles(
            flat_graph, x_min=1, x_max=3, dx=0.5, input_sample_type=side
        )

        for new_rects in rect_list:
            new_rects.set_fill(opacity=0.8)
            rects.align_submobjects(new_rects)
            for alt_rect in rects[1::2]:
                alt_rect.set_fill(opacity=0)
            self.play(Transform(
                rects, new_rects,
                run_time=2,
                lag_ratio=0.5
            ))
        self.wait()

    def func(self, x):
        return (x-3) ** 3 + (x - 3) ** 2-2*(x-3) + 1


"""
class AreaUnderVGraph(PlotVelocity):
    def construct(self):
        self.setup_axes()
        self.add(*self.get_v_graph_and_label())
        self.show_rects()

    def show_rects(self):
        rect_list = self.get_riemann_rectangles_list(
            self.v_graph, 7,
            max_dx=1.0,
            x_min=0,
            x_max=8,
        )
        flat_graph = self.get_graph(lambda t: 0)
        rects = self.get_riemann_rectangles(
            flat_graph, x_min=0, x_max=8, dx=1.0
        )

        for new_rects in rect_list:
            new_rects.set_fill(opacity=0.8)
            rects.align_submobjects(new_rects)
            for alt_rect in rects[::2]:
                alt_rect.set_fill(opacity=0)
            self.play(Transform(
                rects, new_rects,
                run_time=2,
                lag_ratio=0.5
            ))
        self.wait()
"""
