import os
import pandas as pd
from flask import Flask, render_template

template_path = os.path.abspath("./frontend/templates")
app = Flask(__name__, template_folder=template_path)

# Charge Data
df = pd.read_csv("backend\src\wheather_data\stations.txt",skiprows=17)

@app.route("/")
def home():
    return render_template("home.html", data=df[["STAID","STANAME"]].to_html())

@app.route("/api/v1/<station>/<date>")
def weather_api(station,date):
    try:
        path = f"backend\src\wheather_data\TG_STAID{int(station):06d}.txt"
        df = pd.read_csv(path,parse_dates=["DATE"],skiprows=20)
        temperature = str(df.loc[df["DATE"] == date]["TG"].squeeze() / 10)

        return {"Station": station,
            "Date": date,
            "temperature":temperature}
    except FileNotFoundError:
        return "Not Existing Data"

if __name__ == "__main__":
    app.run(debug=True)