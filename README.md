# Mandelbrot Generator

This program generates a Mandelbrot set image based on user input.

## Requirements

To run the program, ensure you have the following:

- Python (version 3 or above)
- Tkinter library (`pip install tkinter`)
- PIL library (`pip install pillow`)

## Usage

1. Open the Python script `main.py` in your preferred Python IDE or text editor.
2. Run the script.
3. A window titled "Mandelbrot Generator" will appear.
4. Enter the desired number of iterations in the provided entry field.
5. Select the desired size of the image by clicking one of the three buttons: Small, Medium, or Large.
6. Click the "Generate!" button to generate the Mandelbrot set image.
7. The generated image will be displayed in a new window.

## Files

- `main.py`: Contains the main program logic and the user interface using Tkinter.
- `mandelbrot.py`: Contains the Mandelbrot class, which defines methods for generating the Mandelbrot set image.

## Mandelbrot Class

The `Mandelbrot` class in `mandelbrot.py` implements the logic for generating the Mandelbrot set image.

### Methods

- `__init__(self, max_iterations)`: Constructor for the Mandelbrot class. Initializes the maximum number of iterations.
- `inSet(self, c)`: Checks if a value is part of the Mandelbrot set.
- `ratio(self, c)`: Determines the stability ratio of the given value `c` in the Mandelbrot set. The closer the ratio is to 1, the more stable the value is.
- `escape_count(self, c)`: Finds the escape count if the given value `c` diverges; otherwise, returns the maximum number of iterations.

## Results

The program generates a Mandelbrot set image based on user input. The size of the image can be selected as Small, Medium, or Large. The number of iterations determines the level of detail in the generated image. The higher the number of iterations, the more precise the image becomes.

