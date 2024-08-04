import os
import pandas as pd
from flask import Flask, render_template

template_path = os.path.abspath("./frontend/templates")
app = Flask(__name__, template_folder=template_path)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def weather_api(station,date):
    #df = pd.read_csv("")
    temperature = str(23)

    return {"Station": station,
            "Date": date,
            "temperature":temperature}

if __name__ == "__main__":
    app.run(debug=True)