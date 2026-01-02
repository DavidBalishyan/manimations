from manim import *
import random

class Main(Scene):
    def construct(self):
        # Set background to dark blue (night sky)
        self.camera.background_color = "#0a1128"
        
        # Title
        title = Text("New Year's Eve", font_size=60, gradient=(BLUE, PURPLE))
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Countdown numbers
        countdown_numbers = [3, 2, 1]
        for num in countdown_numbers:
            number = Text(str(num), font_size=120, color=YELLOW)
            self.play(FadeIn(number, scale=0.5))
            self.play(number.animate.scale(1.3), rate_func=there_and_back, run_time=0.8)
            self.play(FadeOut(number, scale=2))
        
        # Happy New Year message
        self.play(FadeOut(title))
        happy_new_year = Text("Happy New Year!", font_size=72, gradient=(GOLD, YELLOW))
        year_2026 = Text("2026", font_size=96, color=GOLD, weight=BOLD)
        year_2026.next_to(happy_new_year, DOWN, buff=0.5)
        
        self.play(Write(happy_new_year), run_time=1)
        self.play(FadeIn(year_2026, shift=UP))
        
        # Create fireworks
        self.create_fireworks(5)
        
        # Sparkle effect around text
        self.add_sparkles(happy_new_year, year_2026)
        
        self.wait(2)
        
        # Finale - everything pulses
        self.play(
            happy_new_year.animate.scale(1.2),
            year_2026.animate.scale(1.2),
            rate_func=there_and_back,
            run_time=1
        )
        
        self.wait()
    
    def create_fireworks(self, num_fireworks):
        """Create colorful firework animations"""
        firework_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
        
        for _ in range(num_fireworks):
            # Random position for each firework
            x = random.uniform(-5, 5)
            y = random.uniform(-2, 2)
            center = np.array([x, y, 0])
            
            # Create firework burst
            num_lines = 16
            lines = VGroup()
            for i in range(num_lines):
                angle = i * TAU / num_lines
                line = Line(
                    center,
                    center + np.array([np.cos(angle), np.sin(angle), 0]) * 0.01,
                    color=random.choice(firework_colors),
                    stroke_width=3
                )
                lines.add(line)
            
            # Animate firework explosion
            self.play(
                *[line.animate.put_start_and_end_on(
                    center,
                    center + (line.get_end() - line.get_start()) * 100
                ) for line in lines],
                run_time=0.6,
                rate_func=rush_from
            )
            self.play(FadeOut(lines), run_time=0.4)
    
    def add_sparkles(self, *mobjects):
        """Add sparkle effects around mobjects"""
        sparkles = VGroup()
        for _ in range(20):
            x = random.uniform(-6, 6)
            y = random.uniform(-3, 3)
            sparkle = Star(
                n=5,
                outer_radius=0.1,
                color=random.choice([YELLOW, GOLD, WHITE]),
                fill_opacity=1
            ).move_to([x, y, 0])
            sparkles.add(sparkle)
        
        self.play(
            LaggedStart(
                *[FadeIn(s, scale=0.5) for s in sparkles],
                lag_ratio=0.1
            ),
            run_time=1
        )
        self.play(
            *[s.animate.scale(1.5).set_opacity(0) for s in sparkles],
            run_time=1.5
        )
        self.remove(sparkles)
