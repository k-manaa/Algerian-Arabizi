import pandas as pd
from collections import Counter
from tqdm import tqdm

def keep_most_frequent_transliterations(df_chunk):
    # Drop rows with NaN values in 'Arabizi' or 'Arabic'
    df_chunk = df_chunk.dropna(subset=['Arabizi', 'Arabic'])
    
    # Ensure 'Arabic' column contains strings only
    df_chunk['Arabic'] = df_chunk['Arabic'].astype(str)

    # Group by 'Arabizi' and create a Counter for each group
    transliteration_counts = df_chunk.groupby('Arabizi')['Arabic'].apply(lambda x: Counter(x)).to_dict()

    rows_to_keep = []
    for arabizi, arabic_counts in transliteration_counts.items():
        if not isinstance(arabic_counts, Counter):
            print(f"Skipping {arabizi} as its counts is not a Counter object: {arabic_counts}")
            continue

        most_common = arabic_counts.most_common()
        if not most_common:
            print(f"No common transliterations found for {arabizi}")
            continue

        highest_frequency = most_common[0][1]

        # Get all transliterations with the highest frequency
        most_frequent_transliterations = [t for t, freq in most_common if freq == highest_frequency]

        for arabic in most_frequent_transliterations:
            try:
                rows_to_keep.append(df_chunk[(df_chunk['Arabizi'] == arabizi) & (df_chunk['Arabic'] == arabic)].iloc[0])
            except IndexError as e:
                print(f"Index error for Arabizi: {arabizi}, Arabic: {arabic} - {e}")

    return pd.DataFrame(rows_to_keep)

def main():
    file_path = 'preprocessed_arabizi.csv'
    chunk_size = 1000  # Adjust based on your system's memory capacity

    # Determine the total number of rows in the CSV
    total_rows = sum(1 for _ in open(file_path)) - 1  # Subtract 1 for the header row
    total_chunks = (total_rows // chunk_size) + 1

    df_cleaned_chunks = []
    chunks = pd.read_csv(file_path, chunksize=chunk_size)

    for chunk in tqdm(chunks, desc="Processing chunks", total=total_chunks):
        df_cleaned_chunk = keep_most_frequent_transliterations(chunk)
        df_cleaned_chunks.append(df_cleaned_chunk)

    # Concatenate all cleaned chunks
    if df_cleaned_chunks:
        df_cleaned = pd.concat(df_cleaned_chunks, ignore_index=True)
    else:
        df_cleaned = pd.DataFrame(columns=['Arabizi', 'Arabic'])

    # Save the cleaned data to a new CSV file
    output_file_path = 'cleaned_arabizi.csv'
    df_cleaned.to_csv(output_file_path, index=False)

    print(f"Data cleaned and saved to {output_file_path}")

if __name__ == '__main__':
    main()
