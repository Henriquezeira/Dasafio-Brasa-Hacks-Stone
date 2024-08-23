# start.py

from flask import Flask, request, jsonify
from data_processing import download_data, load_data
from data_analysis import analyze_data

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    download_data()
    df = load_data()
    summary_bank, summary_sales = analyze_data(df)
    return jsonify({
        'summary_bank': summary_bank.to_dict(),
        'summary_sales': summary_sales.to_dict()
    })

@app.route('/data_summary', methods=['GET'])
def data_summary():
    df = load_data()
    summary_bank, summary_sales = analyze_data(df)
    return jsonify({
        'summary_bank': summary_bank.to_dict(),
        'summary_sales': summary_sales.to_dict()
    })

if __name__ == '__main__':
    app.run(debug=True)
