import spacy
import pandas as pd

def perform_pos_tagging():
    # Load the small English model
    # Ensure you have run: pip install -r requirements.txt
    try:
        nlp = spacy.load('en_core_web_sm')
    except OSError:
        print("Model not found. Please run: python -m spacy download en_core_web_sm")
        return

    # Sample text (Jane Austen's 'Emma' snippet)
    text = (
        "emma woodhouse handsome clever and rich with a comfortable home and "
        "happy disposition seemed to unite some of the best blessings of existence "
        "and had lived nearly twentyone years in the world with very little to "
        "distress or vex her"
    )
    print(f"Analyzing text:\n{text}\n")

    # Process the text
    doc = nlp(text)

    # Extract tokens and POS tags into a list of dictionaries (more efficient than loop concat)
    data = []
    for token in doc:
        data.append({
            'token': token.text,
            'pos_tag': token.pos_,       # Coarse-grained tag (e.g., NOUN, VERB)
            'tag_desc': token.tag_,      # Fine-grained tag (e.g., NN, VBD)
            'explanation': spacy.explain(token.pos_) # Human readable explanation
        })

    # Create DataFrame
    pos_df = pd.DataFrame(data)

    # Display the first few rows and the full count of tag types
    print("--- Token Analysis DataFrame ---")
    print(pos_df.head(10))
    
    print("\n--- POS Tag Counts ---")
    print(pos_df['pos_tag'].value_counts())

if __name__ == "__main__":
    perform_pos_tagging()