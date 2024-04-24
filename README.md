# 2D Fractal Engine

This repository contains a Python 2D fractal engine implemented using Pygame. It allows you to generate and visualize fractal patterns such as tree fractals and triangle fractals.

## Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [File Structure](#file-structure)
4. [Dependencies](#dependencies)

## Introduction

Fractals are fascinating geometric shapes that exhibit self-similarity at various scales. This fractal engine provides a platform to generate and render 2D fractals in real-time. Currently, it supports two types of fractals:
- Tree Fractals
- Triangle Fractals

The fractals are generated using recursive algorithms and are displayed using Pygame's graphical capabilities.

## Usage

To use the fractal engine, simply run the `main.py` file. This will launch the application window and display the fractal patterns. You can interact with the fractals using keyboard commands:
- Press `SPACE` to finish drawing the fractal pattern.
- Press `ESC` or close the window to exit the application.

## File Structure

The repository contains the following files:

- `main.py`: Contains the main application code including the event loop, initialization, and drawing functions.
- `triangle.py`: Defines the `Triangle_Fractal` class responsible for generating and rendering triangle fractals.
- `factal.py`: Defines the `Tree_Fractal` class responsible for generating and rendering tree fractals.
- `settings.py`: Contains configuration settings such as window dimensions, colors, and frame rate.

## Dependencies

The fractal engine relies on the following dependencies:
- Python (>= 3.6)
- Pygame (>= 2.0.1)

Ensure you have Python and Pygame installed on your system before running the application.
