# Bullshit Bingo Table Generator

## Overview
This script generates a random 5x5 word table from a list of words in the text file bullshit.txt or any list of buzzwords given as argument. It can generate plans ASCII tables or a HTML table. 

It can be used to play the game called [bullshit bingo](https://en.wikipedia.org/wiki/Buzzword_bingo).

## What it Does
1. **Reads words** from `bullshit.txt` - here an example file containing AI/ML terminology, but you can easily generate your own file of buzzwords of your choosing and specify the input file as command line option.

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
Run the script with various options:

### Default (Print to Console use bullshit.txt)
```bash
python bullshit.py
```

### Use Custom Word List
```bash
python bullshit.py --input custom_words.txt
```

### Export to HTML
```bash
python bullshit.py --html output.html
```
This generates a formatted HTML file with embedded CSS styling.

### Combine Options
```bash
python bullshit.py --input my_buzzwords.txt --html output.html
```

## Command-Line Options
- `--input <file>` - Read word list from a custom file (default: `bullshit.txt`)
- `--html <file>` - Export the table to an HTML file instead of printing to console

## Output
Without options, the script prints a formatted 5x5 table of randomly selected words to the console.

With `--html` option, it creates a complete HTML document with:
- Proper HTML structure with doctype and charset declaration
- CSS styling for table borders and cell padding
- A title heading

## File Structure
- `bullshit.py` - Main script
- `bullshit.txt` - Example word list (AI/ML terminology)
- `corp_jargon.txt` - Example word list (corporate jargon)
- `README.md` - This file

## Examples
5x5 Word Table:
```
+------------------+------------------+------------------+------------------+------------------+
| Knowledge Graph  |  Text-to-Speech  |  Conversational  |  Voice Cloning   |  Speech-to-Text  |
|                  |                  |      Agent       |                  |                  |
+------------------+------------------+------------------+------------------+------------------+
|     Few-shot     |      Speech      |     Ontology     |    Generative    | Bayesian Network |
|     Learning     |   Recognition    |                  |   Adversarial    |                  |
|                  |                  |                  |     Network      |                  |
+------------------+------------------+------------------+------------------+------------------+
| Policy Gradient  |  AI Accelerator  |    Artificial    |    Simulated     |    Emotion AI    |
|                  |                  |     General      |    Annealing     |                  |
|                  |                  |   Intelligence   |                  |                  |
+------------------+------------------+------------------+------------------+------------------+
|      Swarm       |  Generative AI   |     Edge AI      |  Meta-learning   | Semi-Supervised  |
|   Intelligence   |                  |                  |                  |     Learning     |
+------------------+------------------+------------------+------------------+------------------+
|     Quantum      |   Intelligent    |  Conversational  |  Data Labeling   | Long Short-Term  |
|    Computing     |    Automation    |        AI        |                  |      Memory      |
+------------------+------------------+------------------+------------------+------------------+
```
### HTML
[bs.html](bs.html)

https://htmlpreview.github.io/?https://github.com/eianlei/bullshit_bingo/blob/main/bs.html

