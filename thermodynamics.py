%%manim -qm -v WARNING TH
def make_system(
            inner=2,
            outer=2.5,
            label="A",
            color=BLUE
        ):
            b_1 = Square(side_length=inner, stroke_width=0, fill_opacity=0)
            b_2 = Square(side_length=outer, stroke_width=0, fill_opacity=0)

            ring = Difference(
                b_2,
                b_1,
                fill_color=color,
                fill_opacity=1,
                stroke_width=0
            )
            text = Text(label).move_to(b_1.get_center())
            return VGroup(ring, b_1, b_2, text)
from manim import *
class TH(Scene):
    def construct(self):
      system_A=make_system()
      system_A.shift(RIGHT * -4)
      system_B = make_system(label="C", color=RED)
      system_B.shift(RIGHT * 4)
      system_C = make_system(label="B", color=YELLOW)
      eq1 = MathTex(r"\rightleftharpoons").scale(1.5)
      eq2 = MathTex(r"\rightleftharpoons").scale(1.5)

        # Systems ke darmiyan
      eq1.move_to((system_A.get_center() - system_B.get_center()) / 4)
      eq2.move_to((system_B.get_center() + system_C.get_center()) / 2)
      #self.add(system_A, system_B, system_C, eq1, eq2)

      self.play(DrawBorderThenFill(system_A))
      self.play(Write(eq1))
      self.play(DrawBorderThenFill(system_C))
      self.play(Write(eq2))
      self.play(DrawBorderThenFill(system_B))

      self.wait()
