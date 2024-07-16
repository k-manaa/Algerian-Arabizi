import pandas as pd
from collections import Counter

# Load the CSV file
input_file = 'ngram_arabizi.csv'
df = pd.read_csv(input_file)

# Count the occurrences of each (Arabizi, Arabic) pair
pair_counter = Counter(zip(df['Arabizi'], df['Arabic']))

# Create a dictionary to store the most common Arabic transliteration for each Arabizi n-gram
most_common_transliteration = {}

for (arabizi, arabic), count in pair_counter.items():
    if arabizi not in most_common_transliteration or count > most_common_transliteration[arabizi][1]:
        most_common_transliteration[arabizi] = (arabic, count)

# Create a filtered list of (Arabizi, Arabic) pairs to keep
filtered_pairs = [(arabizi, arabic) for arabizi, (arabic, _) in most_common_transliteration.items()]

# Create a new DataFrame from the filtered pairs
filtered_df = pd.DataFrame(filtered_pairs, columns=['Arabizi', 'Arabic'])

# Save the filtered results to a new CSV file
output_file = 'unique_ngram_arabizi.csv'
filtered_df.to_csv(output_file, index=False)

print(f"Filtered results saved to '{output_file}'.")
