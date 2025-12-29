from manim import *

# ============================================
# EXAMPLE 1: Basic Shapes and Transforms
# ============================================
class BasicShapes(Scene):
    def construct(self):
        # Create shapes
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        # Set colors
        circle.set_fill(BLUE, opacity=0.5)
        square.set_fill(RED, opacity=0.5)
        triangle.set_fill(GREEN, opacity=0.5)
        
        # Animate shapes appearing
        self.play(Create(circle))
        self.wait(0.5)
        
        # Transform circle to square
        self.play(Transform(circle, square))
        self.wait(0.5)
        
        # Transform to triangle
        self.play(Transform(circle, triangle))
        self.wait()


# ============================================
# EXAMPLE 2: Text and Positioning
# ============================================
class TextAndPosition(Scene):
    def construct(self):
        # Create text
        title = Text("Welcome to Manim!", font_size=48)
        subtitle = Text("Mathematical Animation Engine", font_size=24)
        
        # Position text
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        
        # Animate text
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait()
        
        # Move text around
        self.play(title.animate.shift(LEFT * 2))
        self.play(subtitle.animate.shift(RIGHT * 2))
        self.wait()


# ============================================
# EXAMPLE 3: Mathematical Equations
# ============================================
class MathEquations(Scene):
    def construct(self):
        equation = MarkupText(
            '(a + b)<sup>2</sup> =  a<sup>2</sup> + 2ab + b<sup>2</sup>',
            font_size=60
        )

        # Show equation
        self.play(Write(equation))
        self.wait()

# ============================================
# EXAMPLE 4: Positioning and Arrangement
# ============================================
class PositioningDemo(Scene):
    def construct(self):
        # Create multiple objects
        shapes = VGroup(
            Circle().set_fill(RED, opacity=0.5),
            Square().set_fill(BLUE, opacity=0.5),
            Triangle().set_fill(GREEN, opacity=0.5)
        )
        
        # Arrange in a row
        shapes.arrange(RIGHT, buff=1)
        
        self.play(FadeIn(shapes))
        self.wait()
        
        # Rearrange vertically
        self.play(shapes.animate.arrange(DOWN, buff=0.5))
        self.wait()


# ============================================
# EXAMPLE 5: Graphs and Functions (Need LaTeX installed)
# ============================================
class GraphExample(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4
        )
        
        # Create graph
        graph = axes.plot(lambda x: x**2 - 1, color=BLUE)
        
        # Labels
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Animate
        self.play(Create(axes), Write(labels))
        self.play(Create(graph))
        self.wait()


# ============================================
# EXAMPLE 6: Animation Timing
# ============================================
class AnimationTiming(Scene):
    def construct(self):
        square = Square()
        
        # Different animation speeds
        self.play(Create(square), run_time=2)  # Slow
        self.wait(0.5)
        
        self.play(square.animate.shift(RIGHT * 2), run_time=0.5)  # Fast
        self.wait(0.5)
        
        # Multiple animations at once
        circle = Circle().shift(LEFT * 2)
        self.play(
            FadeIn(circle),
            square.animate.shift(LEFT * 2),
            run_time=1
        )
        self.wait()


# ============================================
# EXAMPLE 7: Colors and Styling
# ============================================
class ColorAndStyle(Scene):
    def construct(self):
        # Different ways to set colors
        circle1 = Circle().set_color(RED)
        circle2 = Circle().set_fill(BLUE, opacity=0.7)
        circle3 = Circle().set_stroke(GREEN, width=8)
        
        circles = VGroup(circle1, circle2, circle3)
        circles.arrange(RIGHT, buff=1)
        
        self.play(FadeIn(circles))
        self.wait()
        
        # Change colors dynamically
        self.play(circle1.animate.set_color(YELLOW))
        self.wait()


# ============================================
# EXAMPLE 8: Complete Scene with Multiple Elements
# ============================================
class CompleteExample(Scene):
    def construct(self):
        # Title
        title = Text("Pythagorean Theorem", font_size=40)
        title.to_edge(UP)
        
        # Equation
        equation = MathTex(r"a^2 + b^2 = c^2")
        equation.next_to(title, DOWN, buff=0.5)
        
        # Right triangle
        triangle = Polygon(
            LEFT * 2 + DOWN,
            RIGHT * 2 + DOWN,
            RIGHT * 2 + UP * 2,
            color=WHITE
        )
        triangle.shift(DOWN * 0.5)
        
        # Animate everything
        self.play(Write(title))
        self.play(Write(equation))
        self.play(Create(triangle))
        self.wait(2)



# ============================================
# Mathematical Equations with LaTeX
# ============================================
class MathEquationsLatex(Scene):
    def construct(self):
        # Create equation
        equation = MathTex(r"e^{i\pi} + 1 = 0")
        equation.scale(2)
        
        # Show equation
        self.play(Write(equation))
        self.wait()
        
        # Transform to another equation
        equation2 = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
        equation2.scale(1.5)
        
        self.play(Transform(equation, equation2))
        self.wait()


