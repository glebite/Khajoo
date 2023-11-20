"""interface.py - an ollama webinterface experiment

References:
https://github.com/jmorganca/ollama/blob/main/docs/api.md
"""
from flask import Flask, render_template, request
from langchain.llms import Ollama


"""
Load up and set the model (later should be selectable)
"""
ollama = Ollama(base_url='http://localhost:11434', model='openhermes2.5-mistral:7b-fp16')
loaded_model = ollama.model


# fire up the flask
app = Flask(__name__)


# Let's do it.
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        
        output_text = send_to_server(input_text)
        
        return render_template('index.html',
                               loaded_model=loaded_model,
                               output_text=output_text,
                               input_text=input_text)
    
    return render_template('index.html',
                           output_text='',
                           input_text='')


def send_to_server(input_text):
    return ollama(input_text)


# run it
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
