# ---------------- 01 ----------------------------
%%manim -v WARNING -r 1920,1080 -qk kcl
from manim import *
class kcl(Scene):
    def construct(self):
        # ---------------- CIRCUIT ----------------
        line  = Line(start=[-5, 0, 0],      end=[0, 0, 0])
        line1 = Line(start=[0, 0, 0],       end=[3.5355, 3.5355, 0])
        line2 = Line(start=[0, 0, 0],       end=[3.5355, -3.5355, 0])
        dot   = Dot(point=[0, 0, 0], color=YELLOW)
      
        circuit = VGroup(line, line1, line2, dot)
        circuit.scale(0.5)
        eq1 = MathTex(r"I_{1}+I_{2}+I_{3}=0")
         # I1 yellow, I2 green, I3 red — eq1 mein color match
        eq1[0][0:2].set_color(YELLOW)   # I_1
        eq1[0][3:5].set_color(GREEN)    # I_2
        eq1[0][6:8].set_color(RED)
        eq1.move_to(DOWN*3)
        eq1.scale(0.7)        # I_3
        self.play(FadeIn(eq1))

        # after scale(0.5):
        # line  : [-2.5,0] → [0,0]
        # line1 : [0,0]    → [1.77, 1.77]
        # line2 : [0,0]    → [1.77,-1.77]

        # ---------------- ARROWS (circuit ke sath scale match) ----
        # I1 — incoming, midpoint of line ≈ [-1.25, 0]
        arrow1 = Arrow(
            start=[-2.0, 0, 0], end=[-0.6, 0, 0],
            buff=0, color=YELLOW,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.35
        )
        lbl1 = MathTex("I_1", color=YELLOW, font_size=38)\
                   .next_to(arrow1, UP, buff=0.12)

        # I2 — upper branch, midpoint ≈ [0.88, 0.88]
        arrow2 = Arrow(
            start=[0.25, 0.25, 0], end=[1.4, 1.4, 0],
            buff=0, color=GREEN,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.35
        )
        lbl2 = MathTex("I_2", color=GREEN, font_size=38)\
                   .next_to(arrow2, UL, buff=0.08)

        # I3 — lower branch, midpoint ≈ [0.88,-0.88]
        arrow3 = Arrow(
            start=[0.25, -0.25, 0], end=[1.4, -1.4, 0],
            buff=0, color=RED,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.35
        )
        lbl3 = MathTex("I_3", color=RED, font_size=38)\
                   .next_to(arrow3, DL, buff=0.08)

        arrows = VGroup(arrow1, lbl1, arrow2, lbl2, arrow3, lbl3)

        # ---------------- ANIMATE CIRCUIT + ARROWS ---------------
        self.play(Create(circuit))
        self.wait(0.4)
        self.play(
            LaggedStart(
                GrowArrow(arrow1), FadeIn(lbl1, shift=UP * 0.2),
                GrowArrow(arrow2), FadeIn(lbl2, shift=UL * 0.2),
                GrowArrow(arrow3), FadeIn(lbl3, shift=DL * 0.2),
                lag_ratio=0.35
            )
        )
        self.wait(1.2)
        g=VGroup(circuit, arrows)
        self.play(FadeOut(g,eq1))
        self.wait(1)
        # ---------------- EQUATIONS1 ----------------
        eq1 = MathTex(r"I_{1}+I_{2}+I_{3}=0")
        eq2 = MathTex(r"I=\frac{dQ}{dt}")
        eq3 = MathTex(r"Q=ne")
        eq4 = MathTex(r"\frac{dQ_{1}}{dt}+\frac{dQ_{2}}{dt}+\frac{dQ_{3}}{dt}=0")
        eq5 = MathTex(r"e\left(\frac{dn_{1}}{dt}+\frac{dn_{2}}{dt}+\frac{dn_{3}}{dt}\right)=0")
        eq6 = MathTex(r"e\neq 0")
        eq7 = MathTex(r"\frac{dn_{1}}{dt}+\frac{dn_{2}}{dt}+\frac{dn_{3}}{dt}=0")
        derivation1 = VGroup(eq1, eq2, eq3, eq4, eq5, eq6, eq7)
        derivation1.scale(0.7)
        derivation1.arrange(DOWN, buff=0.5)
        for eq in derivation1:
            self.play(FadeIn(eq))
            self.wait(0.5)
        self.play(Circumscribe(derivation1[6], color=YELLOW))
        self.wait(2)
        self.play(FadeOut(derivation1))
        self.wait(1)
        # ---------------- EQUATIONS2 ----------------
        eq1 = MathTex(r"\frac{d}{dt}(n_{1}+n_{2}+n_{3})=0")
        eq2 = MathTex(r"N=n_{1}+n_{2}+n_{3}")
        eq3 = MathTex(r"\frac{dN}{dt}=0")     
        derivation2 = VGroup(eq1, eq2, eq3)
        derivation2.scale(0.7)
        derivation2.arrange(DOWN, buff=0.5)
        for eq in derivation2:
            self.play(FadeIn(eq))
            self.wait(0.5)
        self.wait(1)
        self.play(FadeOut(derivation2))
        self.wait(1)
        derivation2[0].move_to(UP*4)
        txt = Text(
    "There are two solutions to this equation:\n"
    "1) N is a positive constant number\n"
    "2) N is zero",
    font_size=20,          # key fix (MathTex ke close)
    line_spacing=0.8       # spacing tight
)
        self.play(Write(txt),FadeIn(derivation2[2]))


