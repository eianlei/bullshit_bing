# Bullshit Bingo Table Generator

## Overview
This script generates a random 5x5 word table from a list of words in the text file bullshit.txt.

It can be used to play the game called [bullshit bingo](https://en.wikipedia.org/wiki/Buzzword_bingo).

## What it Does
1. **Reads words** from `bullshit.txt` - here an example file containing AI/ML terminology, but you can easily generate your own file of buzzwords of your choosing.

2. **Selects 25 random words** from the available words
3. **Shuffles** the selected words randomly
4. **Creates a formatted table** using PrettyTable with the following features:
   - 5 columns × 5 rows layout
   - No header row
   - 80-character width (16 characters per column max)
   - Horizontal borders between each row
5. **Displays the table** with a title

## Requirements
- Python 3.x
- `prettytable` library

## Installation
Install the required dependency:
```bash
pip install prettytable
```

## Usage
Run the script:
```bash
python bullshit.py
```

## Output
The script prints a formatted 5x5 table of randomly selected words from the word list.

## File Structure
- `bullshit.py` - Main script
- `bullshit.txt` - Word list (AI/ML terminology)
- `README.md` - This file
