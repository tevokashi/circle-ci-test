from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    """Hello World

    Returns:
        [string] -- Ola mundo
    """
    return "Ola mundo!"