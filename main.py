import json

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/init/object', methods=['GET'])
def init_object():
    with open('init_object.json', 'r') as f:
        json_data = json.load(f)
    return jsonify(json_data)

if __name__=="__main__":
    app.run()