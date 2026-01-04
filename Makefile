.PHONY: help install clean venv-install

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install          Create venv and install dependencies."
	@echo "  venv-install     Create virtual environment and install manim into it."
	@echo "  gauss            Render the gauss animation."
	@echo "  new_year         Render the new_year animation."
	@echo "  main             Render all animations in main.py."
	@echo "  clean            Remove generated files."
	@echo ""
	@echo "Individual scenes from main.py:"
	@echo "  make basic_shapes"
	@echo "  make text_and_position"
	@echo "  make math_equations"
	@echo "  make positioning_demo"
	@echo "  make graph_example"
	@echo "  make animation_timing"
	@echo "  make color_and_style"
	@echo "  make complete_example"
	@echo "  make math_equations_latex"

venv-install:
	@echo "Creating virtual environment and installing manim..."
	python3 -m venv .venv
	./.venv/bin/pip install manim

install: venv-install

gauss:
	./.venv/bin/python3 -m manim -pqh gauss.py Main

new_year:
	./.venv/bin/python3 -m manim -pqh new_year.py Main

main:
	./.venv/bin/python3 -m manim -pqh main.py

basic_shapes:
	./.venv/bin/python3 -m manim -pqh main.py BasicShapes

text_and_position:
	./.venv/bin/python3 -m manim -pqh main.py TextAndPosition

math_equations:
	./.venv/bin/python3 -m manim -pqh main.py MathEquations

positioning_demo:
	./.venv/bin/python3 -m manim -pqh main.py PositioningDemo

graph_example:
	./.venv/bin/python3 -m manim -pqh main.py GraphExample

animation_timing:
	./.venv/bin/python3 -m manim -pqh main.py AnimationTiming

color_and_style:
	./.venv/bin/python3 -m manim -pqh main.py ColorAndStyle

complete_example:
	./.venv/bin/python3 -m manim -pqh main.py CompleteExample

math_equations_latex:
	./.venv/bin/python3 -m manim -pqh main.py MathEquationsLatex

clean:
	rm -rf media .venv __pycache__
