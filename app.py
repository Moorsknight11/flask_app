from flask import Flask, render_template, request, redirect, url_for, Response
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests


from flask import jsonify


app = Flask(__name__)

# DB connection (replace with your credentials)
# username = 'root'
# password = ''
# host = 'localhost'
# database = 'test'

# engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
@app.route("/delegations")
def get_delegations():
    code_gov = request.form.get("code_gouvernorat")
    
    response = requests.get("https://moors.rf.gd/query.php", params={
        "code_gov": code_gov,

    })

    if response.status_code != 200: 
        return "Failed to fetch data", 500

    data = response.json()
    df = pd.DataFrame(data)
    return jsonify(df.to_dict(orient="records"))

@app.route("/", methods=["POST"])
def index():
    response = requests.get("https://moors.rf.gd/query.php", params={
        "gouvernorats": "all",

    })

    if response.status_code != 200:
        return "Failed to fetch data", 500

    data = response.json()
    gouvernorats_df = pd.DataFrame(data)
    gouvernorats = gouvernorats_df.to_dict(orient='records')
    return render_template("index.html", gouvernorats=gouvernorats, selected_code=None)





if __name__ == "__main__":
    app.run(debug=True)
