# Algerian Arabizi to Standard Arabic Dataset

## Description

This repository contains the code and datasets used for the research and development of transliteration systems and NLP models for Algerian Arabizi, as detailed in the Master's thesis "Exploring the Complexities of Transliteration: A Study on Algerian Arabizi" by Khadidja Manaa at the University of Zurich, under the supervision of Prof. Dr. Gerold Schneider.

The thesis explores the complexities of transliteration, particularly focusing on Algerian Arabizi—a blend of Arabic and Latin letters used in digital communication by millions of users. The research highlights the challenges of phonetic transformation when dealing with non-Latin scripts and reviews various transliteration methods from traditional rule-based systems to advanced neural models. Through detailed analyses, the study examines the efficacy of statistical and neural models in handling the inconsistencies and phonetic ambiguities inherent in Algerian Arabizi.

**Very important note:** This dataset was built thanks to the efforts of the respective teams (who will be cited appropriately below). It would greatly benefit from manual annotation and correction!

## Contents

### 1. Code Files:

- `final_preprocessing.py`: 
  - Preprocessing script for preparing the datasets, it cleans the data by retaining only the most frequent transliterations for each 'Arabizi' entry and saves the cleaned results to ‘cleaned_arabizi.csv’.

- `generate_ngrams.py`: 
  - Script to generate n-grams (from 1 up to the length of the text) for each pair of words, and saves all mappings. An example would be the following for the word pair kayen,كاين:
    - k,ك
    - a,ا
    - y,ي
    - e,ن
    - ka,كا
    - ay,اي
    - ye,ين
    - kay,كاي
    - aye,اين
    - kaye,كاين
  - One can already see that the n-grams are of subpar quality, since Arabizi is very inconsistent, and many of the character mappings aren’t directly one to one. 

- `generate_unique_ngrams.py`: 
  - Script to generate unique n-grams; it counts occurrences of each unique (Arabizi, Arabic) pair using Counter, identifies the most common Arabic transliteration for each Arabizi n-gram, and saves the filtered results to ‘unique_ngram_arabizi.csv’. Interestingly, the unique n-gram file has 137912 entries, while the original n-gram file has 1014685 entries (a decrease of 86.41%).

- `visualize.py`: 
  - A visualization script, using pandas and Counter to extract, count, and map Arabizi entries to their corresponding Arabic transliterations. The script then identifies and prints the top 100 most frequently occurring Arabizi entries along with their Arabic counterparts.

### 2. Datasets:

- `unique_ngram_arabizi.csv`: Contains unique n-grams generated from processed_arabizi.csv.

- `ngram_arabizi.csv`: Contains n-grams generated from the processed_arabizi_csv.

- `preprocessed_arabizi.csv`: Preprocessed Arabizi text data. 66197 rows of Algerian Arabizi to Standard Arabic mappings, which are not checked manually, a mix of the datasets below. 

- `preprocessed_dzner.csv`: 
  - Source: Dahou, Abdelhalim, and Mohamed Amine Cheragui. "DzNER Dataset for Named Entity Recognition in Algerian Dialect." Proceedings of the 1st Workshop on Arabic Natural Language Processing, 2023. https://doi.org/10.1007/978-3-031-25344-7_13
  - Preprocessing steps:
    - cleaning, normalizing, tokenizing, and preparing the data for transliteration and word pair generation. Two specific GPT-4 Turbo prompts were utilized to enhance the original DzNER dataset. The first prompt was designed for generating detailed word-to-word mappings between Arabizi and Arabic, instructing GPT-4 Turbo to retain the original word order and meaning while listing the mappings in a consistent format. This prompt was used to create a file containing pairs of corresponding words from both scripts. The second prompt focused on transliteration, asking GPT-4 Turbo to convert entire sentences from Algerian Arabic script to Algerian Arabizi, maintaining the sentence structure and meaning. These prompts were specifically chosen to leverage GPT-4 Turbo's advanced capabilities, ensuring high accuracy and consistency in the dataset enhancements. However, the word order is still wrong in some entries.

- `preprocessed_jordanian.csv`: 
  - Source: Talafha, Bashar, Analle Abu Ammar, and Mahmoud Al-Ayyoub. "Atar: Attention-based LSTM for Arabizi Transliteration." International Journal of Electrical and Computer Engineering (IJECE), vol. 11, no. 3, June 2021, pp. 2327-2334. https://doi.org/10.11591/ijece.v11i3.pp2327-2334.
  - Preprocessing steps:
    - Text cleaning, normalization, standardization to ensure consistency across the dataset, removing special characters, and standardized the spelling of Arabizi words, making the data more uniform and reliable. Additionally, since the original dataset was in Jordanian Arabizi, some character mappings had to be changed manually so that they reflected Algerian Arabizi instead. The changes are as follows:
      - '$' was changed to 'sh' and 'ch'
      - '6' to 't'
      - '9' to 's'
      - "3'" to 'gh' and 'r'
      - "3′" to 'gh' and 'r'
      - "9'" to 'd' and 'dh'
      - "9′" to 'd' and 'dh'
      - '2' to 'a' and '2'
      - '7' to 'h'
      - '5' to 'kh'
      - '8' to 'g', 'k', and 'q'
      - "6'" to 'd', 'dh', and 'th'
      - "6′" to 'd', 'dh', and 'th'
      - '4' to 'th', 'd', and 'dh'
    - Note: these mappings are generated by me and my own experience as a native Algerian Arabizi user.

- `preprocessed_nerdz.csv`: 
  - Source: Touileb, Samia. "{NERD}z: A Preliminary Dataset of Named Entities for Algerian." In Proceedings of the 2nd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language Processing (Volume 2: Short Papers), November 2022, Association for Computational Linguistics, pp. 95-101. https://aclanthology.org/2022.aacl-short.13.
  - Preprocessing steps:
    - Cleaning and normalizing the data, removing unwanted punctuation, converting text to lowercase, and standardizes the text format. Sentence pairs from the NERDz dataset were then extracted, by identifying and aligning pairs of sentences in Algerian Arabizi and their corresponding Arabic translations, ensuring that each pair maintains its original context and meaning.

- `preprocessed_padic.csv`: 
  - Source: Meftouh, Karima, Salima Harrat, Salma Jamoussi, Mourad Abbas, and Kamel Smaili. "Machine Translation Experiments on PADIC: A Parallel Arabic Dialect Corpus." Proceedings of the 29th Pacific Asia Conference on Language, Information and Computation, edited by Hai Zhao, October 2015, Shanghai, China, Association for Computational Linguistics, pp. 26-34. https://aclanthology.org/Y15-1004.
  - Preprocessing steps:
    - Initial preprocessing of Algiers Arabic sentences, where unwanted characters were removed, text was converted to lowercase, and the text format was standardized to ensure consistency. Algiers Arabic sentences were then extracted from the PADIC dataset and aligned with their corresponding MSA translations. MSA sentences were extracted and matched with the Algiers Arabic sentences to ensure accurate translation and transliteration tasks. The extracted translated sentences were further cleaned to remove any remaining inconsistencies, ensuring that both Algiers Arabic and MSA sentences were free from noise. GPT-4 Turbo was then used to generate Arabic and Arabizi scripts, ensuring accurate transliterations. Additionally, word pairs between Arabizi and Arabic were matched. The following prompts were used:
      - "You are an expert in Arabic dialects. Please convert the following Algiers Arabic sentences into Modern Standard Arabic while preserving their original meaning and context: [Algiers Arabic sentence]."
      - "You are an expert in Arabic dialects and transliteration. Please convert the following Algiers Arabic sentences into Arabizi (using Latin script) while preserving their original pronunciation and meaning: [Algiers Arabic sentence]."
      - "You are an expert in Arabic dialects and transliteration. Please provide a word-to-word mapping between the following Algiers Arabic sentence and its Arabizi transliteration: [Algiers Arabic sentence] -> [Arabizi sentence]."

- `preprocessed_tarc.csv`:
  - Source: Gugliotta, Elisa, Marco Dinarelli, and Olivier Kraif. "Multi-Task Sequence Prediction for Tunisian Arabizi Multi-Level Annotation." The Fifth Arabic Natural Language Processing Workshop (WANLP), 2020. https://aclanthology.org/2020.wanlp-1.16.
  - Preprocessing steps:
    - Rows with missing values were removed. Following this, the Arabizi text columns was converted to lowercase, whitespace was removed, diacritics were stripped, and any numerical suffixes were eliminated. Special characters and unwanted patterns were also removed. Further refinement involved removing entries that consisted solely of punctuation or special characters, contained only Arabizi or only Arabic text, or where the Arabizi and Arabic text were identical. This thorough cleaning process significantly reduced the dataset's size but enhanced its quality by focusing on meaningful transliterations. To further refine the data, a function was employed to retain only the highest occurring transliterations for each Arabic entry. This step ensured that the most representative transliterations were preserved, enhancing the dataset's reliability.

## Acknowledgements

This work was supported by the University of Zurich and was supervised by Prof. Dr. Gerold Schneider. Special thanks to all those who contributed directly or indirectly to this research, including Abdelhalim Dahou, Mohamed Amine Cheragui, Bashar Talafha, Analle Abu Ammar, Mahmoud Al-Ayyoub, Samia Touileb, Karima Meftouh, Salima Harrat, Salma Jamoussi, Mourad Abbas, Kamel Smaili, Elisa Gugliotta, Marco Dinarelli, and Olivier Kraif. Your efforts in developing and sharing the datasets have been invaluable to this study.
