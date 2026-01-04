# Manim Animation Collection

This project is a collection of animations created using the [Manim Community](https://www.manim.community/) library.

## Getting Started

### Prerequisites

*   Python 3
*   `pip`

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/DavidBalishyan/manimations.git
    cd manimations
    ```

2.  Create the virtual environment and install the dependencies:
    ```sh
    make install
    ```

## Usage

You can render the animations using the `make` commands defined in the `Makefile`.

### Render all animations in a file

*   Render the Gaussian Integral animation:
    ```sh
    make gauss
    ```

*   Render the New Year animation:
    ```sh
    make new_year
    ```

*   Render all animations in `main.py`:
    ```sh
    make main
    ```

### Render individual scenes from `main.py`

You can also render individual scenes from `main.py`:

*   `make basic_shapes`
*   `make text_and_position`
*   `make math_equations`
*   `make positioning_demo`
*   `make graph_example`
*   `make animation_timing`
*   `make color_and_style`
*   `make complete_example`
*   `make math_equations_latex`


## Cleaning up

To remove the generated `media`, `.venv` and `__pycache__` directories, run:

```sh
make clean
```
