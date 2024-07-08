from manim import *

class first_scene(Scene):
    def construct(self):
        start_point = LEFT + 2*LEFT
        end_point = RIGHT + 2*RIGHT
        between = start_point + (end_point - start_point) / 3
        segment = Line(start_point, end_point, color=ORANGE)
        segment_left = Line(start_point - 0.2*UP, start_point + 0.2*UP, color=ORANGE)
        segment_right = Line(end_point - 0.2*UP, end_point + 0.2*UP, color=ORANGE)
        between_segment = Line(between - 0.2*UP, between + 0.2*UP, color=ORANGE)
        brace_below = Brace(segment, direction = DOWN)
        brace_below.shift(0.8 * DOWN)
        brace_text = brace_below.get_text("1")
        title = Text("Division of the segment in extreme and mean ratio", font_size=24)
        title.to_edge(UP)
        first = VGroup(segment, segment_left, segment_right, between_segment, brace_below)
        self.play(Create(first))
        label_right = Text("x", font_size=30).next_to((start_point + between)/2, UP)
        label_mid = Text("1 - x", font_size=30).next_to((between + end_point)/2, UP)
        self.play(Write(brace_text),
                  Write(label_right),
                  Write(label_mid),
                  Write(title)
                )
        first_all = VGroup(segment,
                          segment_left,
                          segment_right, 
                          between_segment, 
                          brace_below,
                          label_right,
                          label_mid,
                          brace_text,
                          )
        self.wait(2)

        equation_1 = MathTex(r"\frac{1}{x} = \frac{x}{1-x}")
        self.play(TransformMatchingShapes(first_all, equation_1))
        self.wait(2)

        equation_2 = MathTex(r"1 - x = x^2")
        self.play(TransformMatchingShapes(equation_1, equation_2))
        self.wait(2)

        equation_3 = MathTex(r"0=x^2+x-1")
        self.play(TransformMatchingShapes(equation_2, equation_3))
        self.wait(2)

        title_2 = Text("Positive solution of the quadratic function", font_size = 24)
        title_2.to_edge(UP)
        line1 = Text("a = 1", font_size=24)
        line2 = Text("b = 1", font_size=24)
        line3 = Text("c = -1", font_size=24)
        text_group = VGroup(line1, line2, line3).arrange(DOWN, buff=0.5)
        self.play(TransformMatchingShapes(title,title_2))
        self.play(TransformMatchingShapes(equation_3, text_group))
        self.wait(2)

        quad = MathTex(r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", font_size=48)
        self.play(TransformMatchingShapes(text_group, quad))
        self.wait(2)

        quad_2 = MathTex(r"\frac{-1 \pm \sqrt{1^2 - 4.1.(-1)}}{2.1}", font_size=48)
        self.play(TransformMatchingShapes(quad, quad_2))
        self.wait(1)

        quad_3 = MathTex(r"\frac{-1 \pm \sqrt{1 + 4}}{2}", font_size=48)
        self.play(TransformMatchingShapes(quad_2, quad_3))
        self.wait(1)

        quad_4 = MathTex(r"\frac{-1 \pm \sqrt{5}}{2}", font_size=48)
        self.play(TransformMatchingShapes(quad_3, quad_4))
        self.wait(1)

        quad_5 = MathTex(r"\frac{-1 + \sqrt{5}}{2}", font_size=48)
        self.play(TransformMatchingShapes(quad_4, quad_5))
        self.wait(1)

        last = MathTex(r"1, 618...", font_size=48)
        self.play(TransformMatchingShapes(quad_5, last))
        self.wait(2)

        phi_symbol = MathTex(r"\varphi", font_size=160)
        self.play(TransformMatchingShapes(last, phi_symbol))
        self.wait(2)   