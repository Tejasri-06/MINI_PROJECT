from flask import Flask, render_template,request,jsonify
import pandas as pd
from feature import run_feature

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():

    file = request.files['file']
    target_column = request.form['target']

    df = pd.read_csv(file)

    selected_features, accuracy = run_feature(df, target_column)

    feature_names = df.drop(columns=[target_column]).columns
    selected_feature_names = feature_names[selected_features]

    return jsonify({
        "selected_features": list(selected_feature_names),
        "accuracy": round(float(accuracy), 4)
    })

if __name__ == '__main__':
    app.run(debug=True)
