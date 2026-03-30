import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import matplotlib.pyplot as plt
import joblib
import os


# ✅ Safe conversion functions
def safe_float(value, default=0.0):
    try:
        return float(value)
    except:
        return default


def safe_int(value, default=0):
    try:
        return int(value)
    except:
        return default


app = Flask(__name__)
model = joblib.load('model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    int_features = []

    for x in request.form.values():
        try:
            int_features.append(float(x))
        except:
            int_features.append(0.0)

    # Feature transformation
    if int_features[0] == 0:
        f_features = [0, 0, 0] + int_features[1:]
    elif int_features[0] == 1:
        f_features = [1, 0, 0] + int_features[1:]
    elif int_features[0] == 2:
        f_features = [0, 1, 0] + int_features[1:]
    else:
        f_features = [0, 0, 1] + int_features[1:]

    if f_features[6] == 0:
        fn_features = f_features[:6] + [0, 0] + f_features[7:]
    elif f_features[6] == 1:
        fn_features = f_features[:6] + [1, 0] + f_features[7:]
    else:
        fn_features = f_features[:6] + [0, 1] + f_features[7:]

    # Ensure 15 features
    while len(fn_features) < 15:
        fn_features.append(0)

    final_features = [np.array(fn_features)]

    try:
        prediction = model.predict(final_features)
        pred = prediction[0]

        if pred == 0:
            output = 'Normal'
        elif pred == 1:
            output = 'DOS'
        elif pred == 2:
            output = 'PROBE'
        elif pred == 3:
            output = 'R2L'
        else:
            output = 'U2R'

    except Exception as e:
        output = f"Error: {str(e)}"

    return render_template('index.html', prediction=output)


# 🚀 CSV + DASHBOARD
@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']

        if file.filename == '':
            return "No file selected"

        df = pd.read_csv(file)

        predictions = []

        for row in df.values:
            row = list(row)

            while len(row) < 15:
                row.append(0)

            pred = model.predict([np.array(row)])[0]

            if pred == 0:
                label = 'Normal'
            elif pred == 1:
                label = 'DOS'
            elif pred == 2:
                label = 'PROBE'
            elif pred == 3:
                label = 'R2L'
            else:
                label = 'U2R'

            predictions.append(label)

        df['Prediction'] = predictions

        # 📊 Create visualization
        counts = df['Prediction'].value_counts()

        plt.figure()
        counts.plot(kind='bar')
        plt.title("Intrusion Detection Results")
        plt.xlabel("Category")
        plt.ylabel("Count")

        # Save chart
        chart_file = "chart.png"
        plt.savefig(f"static/{chart_file}")
        plt.close()

        return render_template(
            'result.html',
            tables=df.to_html(
                classes='table-auto w-full border border-gray-300', index=False),
            chart=chart_file
        )

    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/results', methods=['POST'])
def results():

    data = request.get_json(force=True)

    try:
        prediction = model.predict([np.array(list(data.values()))])
        pred = prediction[0]

        if pred == 0:
            output = 'Normal'
        elif pred == 1:
            output = 'DOS'
        elif pred == 2:
            output = 'PROBE'
        elif pred == 3:
            output = 'R2L'
        else:
            output = 'U2R'

    except Exception as e:
        output = f"Error: {str(e)}"

    return jsonify(output)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
