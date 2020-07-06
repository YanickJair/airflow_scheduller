from flask import Flask, request

from src.create_config import create_configuration

app = Flask(__name__)

@app.route("/configuartion", methods=['POST'])
def configuration():
    if request.method == 'POST':
        response = create_configuration(request.data)
        return response
    return None