from manim import *

class Main(Scene):
    def construct(self):
        # Title
        title = Text("The Gaussian Integral", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Start with the integral we want to evaluate
        integral = MathTex(r"I = \int_0^\infty e^{-x^2} dx")
        integral.scale(1.5)
        self.play(Write(integral))
        self.wait(2)
        
        # Explain the trick: square it
        explanation1 = Text("Trick: Square both sides", font_size=32)
        explanation1.next_to(integral, DOWN, buff=0.8)
        self.play(Write(explanation1))
        self.wait()
        
        squared = MathTex(r"I^2 = \int_0^\infty e^{-x^2} dx \cdot \int_0^\infty e^{-y^2} dy")
        squared.scale(1.2)
        squared.next_to(explanation1, DOWN, buff=0.5)
        self.play(Write(squared))
        self.wait(2)
        
        # Combine into double integral
        self.play(FadeOut(explanation1))
        double_integral = MathTex(r"I^2 = \int_0^\infty \int_0^\infty e^{-(x^2+y^2)} dx\,dy")
        double_integral.scale(1.2)
        double_integral.move_to(squared)
        self.play(Transform(squared, double_integral))
        self.wait(2)
        
        # Switch to polar coordinates
        explanation2 = Text("Convert to polar coordinates", font_size=32)
        explanation2.next_to(squared, DOWN, buff=0.8)
        self.play(Write(explanation2))
        self.wait()
        
        polar_sub = MathTex(r"x^2 + y^2 = r^2, \quad dx\,dy = r\,dr\,d\theta")
        polar_sub.scale(1.0)
        polar_sub.next_to(explanation2, DOWN, buff=0.3)
        self.play(Write(polar_sub))
        self.wait(2)
        
        # Transform to polar integral
        polar_integral = MathTex(r"I^2 = \int_0^{\pi/2} \int_0^\infty r e^{-r^2} dr\,d\theta")
        polar_integral.scale(1.2)
        polar_integral.next_to(polar_sub, DOWN, buff=0.5)
        self.play(Write(polar_integral))
        self.wait(2)
        
        # Clear and solve the r integral
        self.play(
            FadeOut(integral),
            FadeOut(squared),
            FadeOut(explanation2),
            FadeOut(polar_sub)
        )
        polar_integral.generate_target()
        polar_integral.target.move_to(ORIGIN).shift(UP)
        self.play(MoveToTarget(polar_integral))
        
        # Solve the inner integral
        explanation3 = Text("Solve inner integral with u = r²", font_size=28)
        explanation3.next_to(polar_integral, DOWN, buff=0.5)
        self.play(Write(explanation3))
        self.wait()
        
        solved_r = MathTex(r"I^2 = \int_0^{\pi/2} \left[-\frac{1}{2}e^{-r^2}\right]_0^\infty d\theta = \int_0^{\pi/2} \frac{1}{2} d\theta")
        solved_r.scale(1.0)
        solved_r.next_to(explanation3, DOWN, buff=0.4)
        self.play(Write(solved_r))
        self.wait(2)
        
        # Final evaluation
        final_eval = MathTex(r"I^2 = \frac{1}{2} \cdot \frac{\pi}{2} = \frac{\pi}{4}")
        final_eval.scale(1.3)
        final_eval.next_to(solved_r, DOWN, buff=0.5)
        self.play(Write(final_eval))
        self.wait(2)
        
        # Clear and show final result
        self.play(
            FadeOut(title),
            FadeOut(polar_integral),
            FadeOut(explanation3),
            FadeOut(solved_r)
        )
        final_eval.generate_target()
        final_eval.target.move_to(ORIGIN).shift(UP*0.5)
        self.play(MoveToTarget(final_eval))
        
        # Take square root
        explanation4 = Text("Take the square root", font_size=32)
        explanation4.next_to(final_eval, DOWN, buff=0.8)
        self.play(Write(explanation4))
        self.wait()
        
        # Final answer
        answer = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
        answer.scale(2)
        answer.next_to(explanation4, DOWN, buff=0.5)
        self.play(Write(answer))
        self.wait()
        
        # Highlight the result
        box = SurroundingRectangle(answer, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(2)
        
        # Final note
        self.play(FadeOut(final_eval), FadeOut(explanation4), FadeOut(box))
        answer.generate_target()
        answer.target.move_to(ORIGIN)
        self.play(MoveToTarget(answer))
        
        note = Text("A beautiful result!", font_size=36, color=BLUE)
        note.next_to(answer, DOWN, buff=1)
        self.play(Write(note))
        self.wait(3)
