# Flask backend example (app.py)
from flask import Flask, jsonify
from flask_cors import CORS
import spacy
from collections import Counter

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/data', methods=['GET'])
def get_data():
    
    transcript = ""

    f = open("OutputForBad.txt", "r")
    transcript = f.read()

    # Load spaCy's small English model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using spaCy.
    doc = nlp(transcript)

    # Define sets for fillers.
    strict_fillers = {"um", "uh", "ah"}  # These are almost always fillers.
    ambiguous_fillers = {"like", "so", "basically"}

    # Containers to store results.
    filler_tokens = []
    strong_tokens = []

    # Iterate over tokens in the document.
    for token in doc:
        # Lowercase the token text for matching.
        token_lower = token.text.lower()
        
        if token_lower in strict_fillers:
            # Always mark as filler.
            filler_tokens.append(token.text)
        elif token_lower in ambiguous_fillers:
            # Use POS tagging or dependency label to decide for ambiguous words.
            # Here, we consider the token a filler if it is used as:
            # - An adverb ('ADV'),
            # - An interjection ('INTJ'), or
            # - If its dependency relation suggests a discourse marker (commonly 'discourse' or similar).
            if token.pos_ in {'ADV', 'INTJ'} or token.dep_ in {'discourse'}:
                filler_tokens.append(token.text)
            else:
                strong_tokens.append(token.text)
        else:
            strong_tokens.append(token.text)

    # Compute statistics.
    total_tokens = len(doc)
    filler_count = len(filler_tokens)
    strong_count = len(strong_tokens)

    # Display the results.
    print("Total tokens:", total_tokens)
    print("Filler tokens count:", filler_count)
    print("Filler tokens:", filler_tokens)
    print("Strong tokens count:", strong_count)
    print("Sample of strong tokens:", strong_tokens[:50])  # showing a sample for brevity

    # Optionally, compute ratios.
    filler_ratio = filler_count / total_tokens * 100
    print(f"Filler Ratio: {filler_ratio:.2f}%")
    
    data = {"tokens": total_tokens, "filler_count" : filler_count, "filler_tokens" : filler_tokens}
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)