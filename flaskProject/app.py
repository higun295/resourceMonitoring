from flask import Flask, jsonify, render_template
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/metrics')
def get_metrics():
    cpu_usage = psutil.cpu_percent(interval=5)
    memory_usage = psutil.virtual_memory().percent
    return jsonify(cpu_usage=cpu_usage, memory_usage=memory_usage)

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000)
