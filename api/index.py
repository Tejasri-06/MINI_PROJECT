from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    file = request.files['file']
    target_column = request.form['target']

    # Example processing (replace with your actual logic)
    df = pd.read_csv(file)
    return jsonify({
        "message": "File received successfully",
        "columns": df.columns.tolist(),
        "target": target_column
    })

# Vercel looks for a variable named 'app'