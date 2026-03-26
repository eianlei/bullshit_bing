import random
from prettytable import PrettyTable, ALL

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
table.hrules = ALL

# Add rows to table
for i in range(5):
    row = selected_words[i*5:(i+1)*5]
    table.add_row(row)

# Print the table
print("5x5 Word Table:")
print(table)