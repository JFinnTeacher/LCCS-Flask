# Leaving Cert Computer Science - ALT1 and Flask

This repository is the hub for **ALT1 (Applied Learning Task 1)** in Leaving Certificate Computer Science. It brings together resources for building **interactive websites** with:

- **HTML and CSS** for page structure and styling
- **JavaScript** for interactivity in the browser (buttons, calculators, graphs, user input)
- **Python and Flask** for connecting a web page to Python code and to data stored in CSV files

## What's in this repo

The repo contains **sample code and example sites** you can open, run and adapt for your own projects.

| Folder | What it contains |
| --- | --- |
| [`Assets/HTML_JS Example Files`](Assets/HTML_JS%20Example%20Files) | Small HTML and JavaScript examples: buttons, loops, output, a calculator, a temperature converter and graphing examples |
| [`Assets/Spurs Info System`](Assets/Spurs%20Info%20System) | A full Flask example site that reads football data from a CSV file, takes a survey through a web form and draws a graph with matplotlib |
| [`BasicFlaskExample`](BasicFlaskExample) | A minimal Flask app that reads from and writes to a CSV file from a web page, with step-by-step notes |
| [`Flask Sample`](Flask%20Sample) | A starter Flask project to build on |
| [`Assets/November26CPL`](Assets/November26CPL) | Workshop materials, sample data and the running order from the November 2026 CPL session |

## Running a Flask example

1. Install Flask (and matplotlib for the graph examples):
   ```
   pip install flask matplotlib
   ```
2. Run the example's Python file, for example:
   ```
   python "Assets/Spurs Info System/Football Data.py"
   ```
3. Open the address shown in the terminal (for example `http://127.0.0.1:8080`) in your browser.

If a page shows **500 Internal Server Error**, check the terminal where Flask is running. The full error message is printed there.

The HTML and JavaScript examples don't need Flask. Open the `.html` file in a browser.

## Wiki

The [project wiki](https://github.com/JFinnTeacher/LCCS-Flask/wiki) will be updated over time with guides, tips and other information relevant to ALT1, Flask and JavaScript.
