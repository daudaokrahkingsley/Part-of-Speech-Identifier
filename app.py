
from flask import Flask, render_template, request
import spacy

app = Flask(__name__)



# Load the English language model
nlp = spacy.load("en_core_web_sm")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['word']
        doc = nlp(word)
        pos = doc[0].pos_
        pos_name = doc[0].pos_
        return render_template('index.html', pos=pos_name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
