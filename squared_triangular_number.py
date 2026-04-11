from manim import *

# Color palette
C_GOLD    = "#F5C518"
C_TEAL    = "#00B4D8"
C_CORAL   = "#FF6B6B"
C_PURPLE  = "#9B5DE5"
C_GREEN   = "#06D6A0"
C_ORANGE  = "#FF9F1C"
C_BG      = "#0D1117"
C_TEXT    = "#E6EDF3"
C_GRAY    = "#8B949E"

CUBE_COLORS = [C_TEAL, C_CORAL, C_PURPLE, C_GREEN, C_ORANGE, C_GOLD]


class NicomachusTheorem(Scene):
    def construct(self):
        self.camera.background_color = C_BG

        self.intro()
        self.statement()
        self.numeric_demo()
        self.visual_proof()
        self.formula_reveal()
        self.outro()

    # ── 1. Title ──────────────────────────────────────────────────────────────
    def intro(self):
        title = Text("Nicomachus' Theorem", font_size=56,
                     color=C_GOLD, weight=BOLD)
        subtitle = Text("The Squared Triangular Number", font_size=30,
                        color=C_GRAY)
        subtitle.next_to(title, DOWN, buff=0.4)

        border = SurroundingRectangle(
            VGroup(title, subtitle), color=C_GOLD,
            corner_radius=0.2, buff=0.35
        )
        border.set_stroke(width=2)

        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(subtitle, shift=UP*0.3), Create(border), run_time=1)
        self.wait(1.2)
        self.play(FadeOut(VGroup(title, subtitle, border)))

    # ── 2. State the theorem ──────────────────────────────────────────────────
    def statement(self):
        words = Text(
            "The sum of the first  n  cubes\n"
            "equals the square of the  n-th triangular number.",
            font_size=32, color=C_TEXT, line_spacing=1.5
        ).to_edge(UP, buff=0.7)

        # Main elegant form
        formula = MathTex(
            r"\sum_{k=1}^{n} k^3",
            r"\ =\ ",
            r"\left(\sum_{k=1}^{n} k\right)^{\!2}",
            font_size=52
        )
        formula[0].set_color(C_TEAL)
        formula[1].set_color(C_TEXT)
        formula[2].set_color(C_GOLD)
        formula.next_to(words, DOWN, buff=0.8)

        # Show equivalence to closed form
        equiv = MathTex(
            r"\text{since}\ \sum_{k=1}^{n} k = \frac{n(n+1)}{2},\quad"
            r"\text{this equals}\ \left(\frac{n(n+1)}{2}\right)^{\!2}",
            font_size=28, color=C_GRAY
        ).next_to(formula, DOWN, buff=0.6)

        self.play(FadeIn(words, shift=DOWN*0.3))
        self.wait(0.5)
        self.play(Write(formula), run_time=2)
        self.wait(0.5)
        self.play(FadeIn(equiv, shift=UP*0.2))
        self.wait(2)
        self.play(FadeOut(VGroup(words, formula, equiv)))

    # ── 3. Numeric demo for n = 1..4 ─────────────────────────────────────────
    def numeric_demo(self):
        header = Text("Let's verify for small values of n",
                      font_size=32, color=C_GOLD).to_edge(UP, buff=0.5)
        self.play(Write(header))

        rows = []
        for n in range(1, 5):
            cube_sum = sum(k**3 for k in range(1, n+1))
            T = n*(n+1)//2
            row = MathTex(
                rf"n={n}: \quad",
                rf"\sum_{{k=1}}^{{{n}}} k^3 = {cube_sum}",
                rf"\quad=\quad T_{n}^2 = {T}^2 = {T**2}",
                font_size=32
            )
            row[0].set_color(C_GRAY)
            row[1].set_color(CUBE_COLORS[n-1])
            row[2].set_color(C_GOLD)
            rows.append(row)

        rows_vg = VGroup(*rows).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        rows_vg.next_to(header, DOWN, buff=0.6)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT*0.3), run_time=0.6)
            self.wait(0.3)

        self.wait(1.5)
        self.play(FadeOut(header), FadeOut(rows_vg))

    # ── 4. Visual proof via the L-shaped gnomon argument ─────────────────────
    def visual_proof(self):
        title = Text("Visual Proof  (n = 4)", font_size=36, color=C_GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        idea = Text(
            "Arrange dots in a triangular grid.\n"
            "Each k-th gnomon (L-shape) contains exactly k³ dots.",
            font_size=26, color=C_TEXT, line_spacing=1.4
        ).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(idea))
        self.wait(1.5)
        self.play(FadeOut(idea))

        # Build a 10×10 grid of dots representing T_4 = 10 rows/cols
        # Each gnomon k covers a border of k rows and k cols → k² squares
        # We color gnomon k with k different shades to hint "k copies of k²"
        # For clarity we show the T_4 × T_4 = 100 dot square
        # colored by which gnomon it belongs to.
        N = 4
        T = N*(N+1)//2  # = 10
        DOT_R = 0.14
        SPACING = 0.42
        grid_w = (T - 1) * SPACING
        grid_h = (T - 1) * SPACING

        # Determine gnomon ownership: dot (r,c) (0-indexed) belongs to
        # gnomon k where k = max(r,c)+1  ... in the top-left triangle layout
        # but here we simply use the "border" decomposition:
        # gnomon 1: rows/cols 0..0
        # gnomon 2: rows/cols 1..2  (but only the new border)
        # gnomon k: rows/cols (T_{k-1})...(T_k - 1)
        def gnomon_of(r, c):
            for k in range(1, N+1):
                lo = k*(k-1)//2      # T_{k-1}
                hi = k*(k+1)//2 - 1  # T_k - 1
                if lo <= r <= hi and lo <= c <= hi:
                    # inner square of gnomon k
                    inner_lo = (k-1)*k//2
                    inner_hi = (k-1)*(k+1)//2 - 1 if k > 1 else -1
                    if k == 1 or not (inner_lo <= r <= inner_hi and inner_lo <= c <= inner_hi):
                        return k
            return None

        dots = VGroup()
        dot_grid = {}
        origin = LEFT * grid_w/2 + DOWN * grid_h/2 + DOWN*0.3

        for r in range(T):
            for c in range(T):
                pos = origin + RIGHT * c * SPACING + UP * (T-1-r) * SPACING
                k = gnomon_of(r, c)
                color = CUBE_COLORS[k-1] if k else WHITE
                d = Dot(radius=DOT_R, color=color).move_to(pos)
                d.set_opacity(0)
                dots.add(d)
                dot_grid[(r, c)] = d

        self.add(dots)

        # Animate gnomon by gnomon
        for k in range(1, N+1):
            gnomon_dots = []
            for r in range(T):
                for c in range(T):
                    if gnomon_of(r, c) == k:
                        gnomon_dots.append(dot_grid[(r, c)])

            label_pos = origin + RIGHT*(T-0.5)*SPACING + UP*(T - k*(k+1)//2 + k//2)*SPACING
            lbl = MathTex(rf"k^3={k}^3={k**3}", font_size=22,
                          color=CUBE_COLORS[k-1])
            lbl.next_to(dots, RIGHT, buff=0.15).shift(
                UP * ((N - k + 0.5) * SPACING * k * 0.5))

            self.play(
                *[d.animate.set_opacity(1) for d in gnomon_dots],
                FadeIn(lbl),
                run_time=0.7
            )
            self.wait(0.3)

        # Total label
        total = MathTex(
            r"\text{Total dots} = 10^2 = \left(\frac{4\cdot5}{2}\right)^2 = 100",
            font_size=30, color=C_GOLD
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(total), run_time=1.2)
        self.wait(2)
        self.play(FadeOut(VGroup(title, dots, total)),
                  *[FadeOut(m) for m in self.mobjects])

    # ── 5. Algebraic proof sketch ─────────────────────────────────────────────
    def formula_reveal(self):
        title = Text("Algebraic Proof by Induction",
                     font_size=36, color=C_GOLD).to_edge(UP, buff=0.5)
        self.play(Write(title))

        steps = [
            (r"\textbf{Base case:}\ n=1", C_TEAL),
            (r"1^3 = 1 = \left(\frac{1\cdot2}{2}\right)^2 \checkmark", C_TEXT),
            (r"\textbf{Inductive step:}\ \text{assume true for }n", C_CORAL),
            (r"\sum_{k=1}^{n+1} k^3 = \left(\frac{n(n+1)}{2}\right)^{\!2} + (n+1)^3", C_TEXT),
            (r"= (n+1)^2\!\left[\frac{n^2}{4} + (n+1)\right]", C_TEXT),
            (r"= (n+1)^2 \cdot \frac{n^2+4n+4}{4}", C_TEXT),
            (r"= \left(\frac{(n+1)(n+2)}{2}\right)^{\!2} \checkmark", C_GREEN),
            (r"\therefore\ \sum_{k=1}^{n} k^3 = \left(\sum_{k=1}^{n} k\right)^{\!2}",
             C_GOLD),
        ]

        mobs = []
        prev = title
        for tex, color in steps:
            m = MathTex(tex, font_size=30).set_color(color)
            m.next_to(prev, DOWN, buff=0.28, coor_mask=np.array([0,1,0]))
            m.to_edge(LEFT, buff=0.9) if "textbf" in tex or r"\therefore" in tex \
                else m.shift(RIGHT * 0.6)
            mobs.append(m)
            prev = m

        for m in mobs:
            self.play(Write(m), run_time=0.7)
            self.wait(0.15)

        self.wait(2)

        box = SurroundingRectangle(mobs[-1], color=C_GOLD, corner_radius=0.15, buff=0.15)
        self.play(Create(box))
        self.wait(2)
        self.play(*[FadeOut(o) for o in self.mobjects])

    # ── 6. Outro ──────────────────────────────────────────────────────────────
    def outro(self):
        line1 = Text("Nicomachus' Theorem", font_size=48,
                     color=C_GOLD, weight=BOLD)
        line2 = MathTex(
            r"\sum_{k=1}^{n} k^3 = \left(\sum_{k=1}^{n} k\right)^{\!2}",
            font_size=44, color=C_TEAL
        )
        line3 = Text("Proved  ∎", font_size=32, color=C_GREEN)

        vg = VGroup(line1, line2, line3).arrange(DOWN, buff=0.5)
        self.play(FadeIn(line1, scale=0.8))
        self.play(Write(line2))
        self.play(FadeIn(line3, scale=1.2))
        self.wait(2.5)
        self.play(FadeOut(vg))
