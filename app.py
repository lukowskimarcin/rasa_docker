from flask import Flask, jsonify
from flask import request
from rasa.nlu.model import Interpreter
import tarfile
import shutil

def load_interpreter(model_path):
    tar = tarfile.open(model_path, "r:gz")
    tar.extractall(path="./models/unpack")
    tar.close()
    interpreter = Interpreter.load("./models/unpack/nlu")
    shutil.rmtree("./models/unpack")
    return interpreter

app = Flask(__name__)
interpreter = load_interpreter("./models/nlu-20200814-182845.tar.gz")

@app.route('/') 
def index():
    return "Hello, World!"

@app.route('/interpreter', methods=['POST'])
def get_text_info():
    tmp = request.json['text']
    response = interpreter.parse(tmp)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)