import random
from prettytable import PrettyTable, HRuleStyle

# Read words from file and select 25 random words
with open('bullshit.txt', 'r') as f:
    words = [line.strip() for line in f if line.strip()]

selected_words = random.sample(words, min(25, len(words)))
random.shuffle(selected_words)

# Create PrettyTable without headers
table = PrettyTable()
table.field_names = ["Col1", "Col2", "Col3", "Col4", "Col5"]
table.header = False
table.max_width = 16
table.padding_width = 1
table.hrules = HRuleStyle.ALL

# Calculate max lines needed for any cell
max_lines = 1
for word in selected_words[:25]:
    lines_needed = (len(word) + 15) // 16
    max_lines = max(max_lines, lines_needed)

# Add rows with padding to match tallest row
for i in range(5):
    row = selected_words[i*5:(i+1)*5]
    padded_row = []
    for word in row:
        lines_for_word = (len(word) + 15) // 16
        padding_lines = max_lines - lines_for_word
        padded_word = word + '\n' * padding_lines
        padded_row.append(padded_word)
    table.add_row(padded_row)

# Print the table
print("5x5 Bullshit BINGO Table:")
print(table)
