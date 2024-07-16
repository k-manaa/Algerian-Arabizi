import pandas as pd
from collections import Counter

# Load the CSV file
df = pd.read_csv('unique_ngram_arabizi.csv')

# Extract Arabizi and Arabic words
arabizi_words = df['Arabizi'].tolist()
arabic_words = df['Arabic'].tolist()

# Count the occurrences of each Arabizi entry
arabizi_counter = Counter(arabizi_words)

# Create a mapping of Arabizi to Arabic with correct counts
arabizi_to_arabic = {}
for arabizi, arabic in zip(arabizi_words, arabic_words):
    if arabizi not in arabizi_to_arabic:
        arabizi_to_arabic[arabizi] = arabic

# Get the top 100 most occurring Arabizi entries
top_100_arabizi = arabizi_counter.most_common(500)

# Debugging: Check the actual counts for specific pairs
for arabizi, count in top_100_arabizi:
    arabic = arabizi_to_arabic.get(arabizi, 'N/A')
    print(f"{arabizi}: {arabic} - Count: {count}")

# Print the top 100 most occurring Arabizi entries along with their Arabic transliterations
print(f"\n{'Arabizi':<20} {'Arabic':<20} {'Occurrences':<10}")
print("-" * 50)
for arabizi, count in top_100_arabizi:
    arabic = arabizi_to_arabic.get(arabizi, 'N/A')
    print(f"{arabizi:<20} {arabic:<20} {count:<10}")
