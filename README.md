# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.10.12

To install and run Spacewalks you will need have Python >=3.10.12 
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation

## Installation Instructions

```
# Clone the github repository
git clone git@github.com:hmrodrigues99/spacewalks.git
cd spacewalks

# Create a python virtual environment
python3 -m venv venv_spacewalks
# Linux only - Activate the virtual environment
source venv_spacewalks/bin/activate
# Windows only - Activate the virtual environment
source venv_spacewalks/Scripts/activate

# Install the necessary dependencies
python3 -m pip install -r requirements.txt
```

## Simple Usage Example

To run the analysis using the `eva_data_analysis.py` script from the command line terminal,
launch the script using Python as follows:

```
# Usage Examples
python3 eva_data_analysis.py eva-data.json eva-data.csv
```

The first argument is the path for the JSON input file
The second argument is the path for the output CSV file