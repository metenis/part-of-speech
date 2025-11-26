# POS Tagging with spaCy

This project performs Part-of-Speech (POS) tagging on a sample text from Jane Austen's Emma. It utilizes the spaCy NLP library to parse text and Pandas to structure the output for analysis.

# Prerequisites

Python 3.8 or higher

Installation

Clone or download this repository.

Install dependencies:
This script requires spacy, pandas, and a specific English language model (en_core_web_sm). You can install all of them at once using the provided requirements file:

pip install -r requirements.txt


Note: The requirements file includes a direct link to the model wheel, so you do not need to run a separate python -m spacy download command.

# Usage

Run the script from your terminal:

python pos_tagging.py


# Output

The script will:

Print the raw text being analyzed.

Generate a DataFrame containing:

Token: The individual word.

POS Tag: The coarse-grained part of speech (e.g., NOUN, VERB).

Tag Desc: The fine-grained tag (e.g., NN, VBD).

Explanation: A human-readable description of the tag.

Display the first 10 rows of the analysis.

Print a summary count of all POS tags found in the text.
