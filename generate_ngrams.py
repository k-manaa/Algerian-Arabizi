import pandas as pd

def generate_ngrams(text, n, include_space=True):
    """Generate n-grams from the provided text."""
    ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
    if not include_space:
        # Filter out n-grams that start or end with whitespace
        ngrams = [ng for ng in ngrams if not (ng.startswith(' ') or ng.endswith(' '))]
    return ngrams

def process_text(arabizi, arabic):
    """Process each Arabizi and Arabic word pair to extract all possible n-grams and their mappings."""
    max_length = max(len(arabizi), len(arabic))
    mappings = []
    # Determine if spaces should be included based on whether the entry is more likely a sentence
    include_space = ' ' in arabizi.strip() and len(arabizi.strip().split()) > 1
    for n in range(1, max_length+1):
        arabizi_ngrams = generate_ngrams(arabizi, n, include_space)
        arabic_ngrams = generate_ngrams(arabic, n, include_space)
        limit = min(len(arabizi_ngrams), len(arabic_ngrams))
        for i in range(limit):
            mappings.append((arabizi_ngrams[i], arabic_ngrams[i]))
    return mappings

def main():
    # Load the CSV file
    df = pd.read_csv('preprocessed_arabizi.csv')

    # Fill NaN values with an empty string
    df.fillna('', inplace=True)

    # Create a new DataFrame to hold all mappings
    all_mappings = []

    # Process each row in the DataFrame
    for idx, row in df.iterrows():
        arabizi = row['Arabizi'].strip().lower()  # Normalize the Arabizi text
        arabic = row['Arabic'].strip()            
        mappings = process_text(arabizi, arabic)
        all_mappings.extend(mappings)
    
    # Convert the list of tuples into a DataFrame
    result_df = pd.DataFrame(all_mappings, columns=['Arabizi', 'Arabic'])

    # Save to CSV
    result_df.to_csv('ngram_arabizi.csv', index=False)
    print("Mappings saved to 'ngram_arabizi.csv'.")

if __name__ == '__main__':
    main()
