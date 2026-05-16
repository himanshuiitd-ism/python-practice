from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("webpage.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(
        base_dir,
        "data_small",
        "TG_STAID" + str(station).zfill(6) + ".txt"
    )

    print("file path:", filename)
    print("exists:", os.path.exists(filename))

    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

    date = pd.to_datetime(date)

    temperature = df.loc[df["    DATE"] == date, "   TG"].squeeze() / 10

    return {
        "station": station,
        "date": str(date.date()),
        "temperature": temperature
    }

if __name__ == "__main__":
    app.run(debug=True)