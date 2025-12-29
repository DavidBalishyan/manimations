HOW TO RUN THESE EXAMPLES:
==========================

1. Render a specific scene:
   python3 -m manim -pql main.py BasicShapes

2. Render in high quality:
   python3 -m manim -pqh main.py BasicShapes

3. Quality flags:
   -ql : Low quality (fastest)
   -qm : Medium quality
   -qh : High quality
   -qk : 4K quality

4. Other useful flags:
   -p  : Preview after rendering
   -s  : Save last frame as image
   -a  : Render all scenes in file

5. Example commands:
   python3 -m manim -pql main.py TextAndPosition
   python3 -m manim -pqh main.py MathEquations
   python3 -m manim -pqm main.py GraphExample
   python3 -m manim -pqh main.py CompleteExample

COMMON MANIM OBJECTS:
====================
- Shapes: Circle(), Square(), Triangle(), Rectangle()
- Text: Text(), MathTex(), Tex()
- Graphs: Axes(), NumberPlane()
- Groups: VGroup(), Group()

COMMON ANIMATIONS:
==================
- Create(), Write(), FadeIn(), FadeOut()
- Transform(), ReplacementTransform()
- object.animate.method() - for animating changes

POSITIONING:
============
- .to_edge(UP/DOWN/LEFT/RIGHT)
- .shift(direction * amount)
- .next_to(other_object, direction)
- .move_to(location)
- .arrange(direction, buff=spacing)

USEFUL CONSTANTS:
=================
- Directions: UP, DOWN, LEFT, RIGHT
- Colors: RED, BLUE, GREEN, YELLOW, WHITE, BLACK
- Origin: ORIGIN
