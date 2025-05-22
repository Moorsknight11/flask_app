# from flask import Flask, render_template, request, redirect, url_for, Response
# from sqlalchemy import create_engine
# import pandas as pd
# import matplotlib.pyplot as plt
# import io
# import requests
# import cloudscraper

# from flask import jsonify


# app = Flask(__name__)

# # DB connection (replace with your credentials)
# # username = 'root'
# # password = ''
# # host = 'localhost'
# # database = 'test'

# # engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
# @app.route("/delegations")
# def get_delegations():
#     code_gov = request.form.get("code_gouvernorat")
    
#     response = requests.get("https://moors.atwebpages.com/query.php", params={
#         "code_gov": code_gov,

#     })

#     if response.status_code != 200: 
#         return "Failed to fetch data", 500

#     data = response.json()
#     df = pd.DataFrame(data)
#     return jsonify(df.to_dict(orient="records"))

# @app.route("/", methods=["GET", "HEAD"])
# def index():
#     if request.method == "HEAD":
#         return '', 200
#     try:
#         scraper = cloudscraper.create_scraper()
#         response = scraper.get("http://moors.atwebpages.com/query.php", params={"gouvernorats": "all"})
#         print("STATUS:", response.status_code)
#         print("HEADERS:", response.headers)
#         print("RESPONSE TEXT:", response.text[:500])
#         response.raise_for_status()
#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         gouvernorats_df = pd.DataFrame(data)
#         gouvernorats = gouvernorats_df.to_dict(orient='records')
#         return render_template("index.html", gouvernorats=gouvernorats, selected_code=None)
#     except (requests.RequestException, ValueError) as e:
#         return f"Error fetching or parsing data: {e}", 500

   

    

# @app.route("/filter")
# def filter():
#     selected_code = request.form.get("code_gouvernorat")
#     if not selected_code:
#         return redirect(url_for('index'))

#     response = requests.get("https://moors.rf.gd/query.php", params={
#         "gouvernorats": "filter",
#         "selected_code":selected_code

#     })

#     if response.status_code != 200:
#         return "Failed to fetch data", 500

#     data = response.json()
#     gouvernorats_df = pd.DataFrame(data)
#     gouvernorats = gouvernorats_df.to_dict(orient='records')

#     return render_template("index.html", gouvernorats=gouvernorats, selected_code=selected_code)

# def autopct_format(pct, allvals):
#     absolute = int(round(pct / 100. * sum(allvals)))
#     return f"{pct:.1f}%\n({absolute})"

# @app.route("/dlplot.png")
# def dlplot_png():

#     selected_code = request.args.get('code_delegation')
#     sexe = request.args.get('sexe')
#     age = request.args.get('age')
#     if not age or age == "undefined":
#         age = None
#     if not sexe or sexe == "undefined":
#         sexe = None
#     print(selected_code,sexe,age)
#     if sexe=="both" and not age:
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

       
#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "selected_code": selected_code,
#         "sexe":sexe

#     })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)
#         plt.figure(figsize=(6,6))
#         plt.pie(
#         df['total_Population'],
#         labels=df['Sexe'],
#         autopct=lambda pct: autopct_format(pct, df['total_Population']),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe != "both" and not age:
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "selected_code": selected_code,
#         "sexe":sexe,
#     })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)

#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404

#         plt.figure(figsize=(6, 6))
#         plt.bar(df['Sexe'], df['total_Population'], color='skyblue')
#         plt.xlabel('Sexe')
#         plt.ylabel('Population')
#         plt.title(f"Population for Sex: {df.iloc[0]['Sexe']} in Delegation {df['total_Population'][0]}")
    
#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe == "both" and age=="age":
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age":age
#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)

#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404

#         plt.figure(figsize=(20,20))
#         df['label'] = df['Sexe'] + " (" + df['Trancheage'] + ")\n" + df['total_Population'].astype(str)
#         plt.pie(

#         df['total_Population'],
#         labels=df['label'],
#         autopct=lambda pct: autopct_format(pct,''),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe != "both" and age=="noage":
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age" :age

#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)

#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404


     
#         plt.figure(figsize=(20,20))
#         df['label'] = df['Sexe'] +' ('+df['total_Population'].astype(str)+')'
#         plt.pie(

#         df['total_Population'],
#         labels=df['label'],
#         autopct=lambda pct: autopct_format(pct,''),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe != "both" and age=="age":
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age" :age

#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)

#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404


     
#         plt.figure(figsize=(20,20))
#         df['label'] = df['Sexe'] + " (" + df['Trancheage'] + ")\n" + df['total_Population'].astype(str)
#         plt.pie(

#         df['total_Population'],
#         labels=df['label'],
#         autopct=lambda pct: autopct_format(pct,''),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')

            

    


# @app.route("/gvplot.png")
# def gvplot_png():
#     selected_code = request.args.get('code_gouvernorat')
#     sexe = request.args.get('sexe')
#     age = request.args.get('age')
#     if not age or age == "undefined":
#         age = None
#     if not sexe or sexe == "undefined":
#         sexe = None
#     if sexe=="both" and not age:
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

       
#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "gouvernorats":"1",
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age" :age

#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)

#         plt.figure(figsize=(6,6))
#         plt.pie(
#         df['total_Population'],
#         labels=df['Sexe'],
#         autopct=lambda pct: autopct_format(pct, df['total_Population']),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe != "both" and not age:
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "gouvernorats":"1",
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age" :age

#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)

#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404

#         plt.figure(figsize=(6, 6))
#         plt.bar(df['Sexe'], df['total_Population'], color='skyblue')
#         plt.xlabel('Sexe')
#         plt.ylabel('Population')
#         plt.title(f"Population for Sex: {df.iloc[0]['Sexe']} in Gouvernorat {df['total_Population'][0]}")
    
#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe == "both" and age=="age":
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "gouvernorats":"1",
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age" :age

#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)

#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404

#         plt.figure(figsize=(20,20))
#         df['label'] = df['Sexe'] + " (" + df['Trancheage'] + ")\n" + df['total_Population'].astype(str)
#         plt.pie(

#         df['total_Population'],
#         labels=df['label'],
#         autopct=lambda pct: autopct_format(pct,''),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe == "both" and age=="noage":
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "gouvernorats":"1",
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age" :age

#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)

#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404

#         plt.figure(figsize=(20,20))
#         df['label'] = df['Sexe'] +' ('+df['total_Population'].astype(str)+')'
#         plt.pie(

#         df['total_Population'],
#         labels=df['label'],
#         autopct=lambda pct: autopct_format(pct,''),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe != "both" and age=="age":
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "gouvernorats":"1",
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age" :age

#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)
#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404


     
#         plt.figure(figsize=(20,20))
#         df['label'] = df['Sexe'] + " (" + df['Trancheage'] + ")\n" + df['total_Population'].astype(str)
#         plt.pie(

#         df['total_Population'],
#         labels=df['label'],
#         autopct=lambda pct: autopct_format(pct,''),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')
#     elif sexe != "both" and age=="noage":
#         if not selected_code:
#             return "No Code_Gouvernorat provided", 400

#         response = requests.get("https://moors.rf.gd/query.php", params={
#         "gouvernorats":"1",
#         "selected_code": "selected_code",
#         "sexe":sexe,
#         "age" :age

#         })

#         if response.status_code != 200:
#             return "Failed to fetch data", 500

#         data = response.json()
#         df = pd.DataFrame(data)
#         if df.empty:
#             return "No data found for the selected delegation and sex.", 404


     
#         plt.figure(figsize=(20,20))
#         df['label'] = df['Sexe'] +' ('+df['total_Population'].astype(str)+')'
#         plt.pie(

#         df['total_Population'],
#         labels=df['label'],
#         autopct=lambda pct: autopct_format(pct,''),
#         startangle=140
#         )
#         plt.axis('equal')

#         img = io.BytesIO()
#         plt.savefig(img, format='png')
#         plt.close()
#         img.seek(0)
#         return Response(img.getvalue(), mimetype='image/png')




# if __name__ == "__main__":
#     app.run(debug=True)
# if __name__ == "__main__":
# if __name__ == "__main__":
# if __name__ == "__main__":
# if __name__ == "__main__":
from flask import Flask, render_template, request, redirect, url_for, Response
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import io

from flask import jsonify
import os
from dotenv import load_dotenv

# Load .env file

app = Flask(__name__)



load_dotenv()

# Get variables
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
port = 17722


engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

@app.route("/delegations")
def get_delegations():
    code_gov = request.args.get("code_gouvernorat")
    query = """
        SELECT DISTINCT Code_Delegation, Délégations 
        FROM Population 
        WHERE Code_Gouvernorat = %s
    """
    df = pd.read_sql(query, con=engine, params=(code_gov,))
    return jsonify(df.to_dict(orient="records"))

@app.route("/", methods=["GET"])
def index():
    gouvernorats_df = pd.read_sql("SELECT DISTINCT Code_Gouvernorat, Gouvernorat FROM Population", con=engine)
    gouvernorats = gouvernorats_df.to_dict(orient='records')
    return render_template("index.html", gouvernorats=gouvernorats, selected_code=None)

@app.route("/filter", methods=["POST"])
def filter():
    selected_code = request.args.get("code_gouvernorat")
    if not selected_code:
        return redirect(url_for('index'))

    gouvernorats_df = pd.read_sql("SELECT DISTINCT Code_Gouvernorat, Gouvernorat FROM Population", con=engine)
    gouvernorats = gouvernorats_df.to_dict(orient='records')

    return render_template("index.html", gouvernorats=gouvernorats, selected_code=selected_code)

def autopct_format(pct, allvals):
    absolute = int(round(pct / 100. * sum(allvals)))
    return f"{pct:.1f}%\n({absolute})"

@app.route("/dlplot.png")
def dlplot_png():

    selected_code = request.args.get('code_delegation')
    sexe = request.args.get('sexe')
    age = request.args.get('age')
    if not age or age == "undefined":
        age = None
    if not sexe or sexe == "undefined":
        sexe = None
    print(selected_code,sexe,age)
    if sexe=="both" and not age:
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

       
        query = """
        SELECT Sexe, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Delegation = %s
        GROUP BY Sexe
        """
        df = pd.read_sql(query, con=engine, params=(selected_code,))
        print(df.columns)

        df = pd.read_sql(query, con=engine, params=(selected_code,))
        plt.figure(figsize=(6,6))
        plt.pie(
        df['total_Population'],
        labels=df['Sexe'],
        autopct=lambda pct: autopct_format(pct, df['total_Population']),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe != "both" and not age:
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Delegation = %s AND ID_Sexe = %s
        GROUP BY Sexe, ID_Sexe
    """
        df = pd.read_sql(query, con=engine, params=(selected_code, sexe))

        if df.empty:
            return "No data found for the selected delegation and sex.", 404

        plt.figure(figsize=(6, 6))
        plt.bar(df['Sexe'], df['total_Population'], color='skyblue')
        plt.xlabel('Sexe')
        plt.ylabel('Population')
        plt.title(f"Population for Sex: {df.iloc[0]['Sexe']} in Delegation {df['total_Population'][0]}")
    
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe == "both" and age=="age":
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe, Classe_Age, Trancheage, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Delegation = %s
        GROUP BY Sexe, ID_Sexe, Trancheage, Classe_Age
    """
        df = pd.read_sql(query, con=engine, params=(selected_code,))

        if df.empty:
            return "No data found for the selected delegation and sex.", 404

        df = pd.read_sql(query, con=engine, params=(selected_code,))
        print(df.columns)

        df = pd.read_sql(query, con=engine, params=(selected_code,))
        plt.figure(figsize=(20,20))
        df['label'] = df['Sexe'] + " (" + df['Trancheage'] + ")\n" + df['total_Population'].astype(str)
        plt.pie(

        df['total_Population'],
        labels=df['label'],
        autopct=lambda pct: autopct_format(pct,''),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe != "both" and age=="noage":
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Delegation= %s AND ID_Sexe = %s
        GROUP BY Sexe, ID_Sexe, Trancheage
    """
        df = pd.read_sql(query, con=engine, params=(selected_code,sexe))
        if df.empty:
            return "No data found for the selected delegation and sex.", 404


     
        plt.figure(figsize=(20,20))
        df['label'] = df['Sexe'] +' ('+df['total_Population'].astype(str)+')'
        plt.pie(

        df['total_Population'],
        labels=df['label'],
        autopct=lambda pct: autopct_format(pct,''),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe != "both" and age=="age":
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe,Classe_Age, Trancheage, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Delegation =%s AND ID_Sexe = %s
        GROUP BY Sexe, ID_Sexe, Trancheage,Classe_Age
    """
        df = pd.read_sql(query, con=engine, params=(selected_code,sexe))
        if df.empty:
            return "No data found for the selected delegation and sex.", 404


     
        plt.figure(figsize=(20,20))
        df['label'] = df['Sexe'] + " (" + df['Trancheage'] + ")\n" + df['total_Population'].astype(str)
        plt.pie(

        df['total_Population'],
        labels=df['label'],
        autopct=lambda pct: autopct_format(pct,''),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')

            

    


@app.route("/gvplot.png")
def gvplot_png():
    selected_code = request.args.get('code_gouvernorat')
    sexe = request.args.get('sexe')
    age = request.args.get('age')
    if not age or age == "undefined":
        age = None
    if not sexe or sexe == "undefined":
        sexe = None
    if sexe=="both" and not age:
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

       
        query = """
        SELECT Sexe, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Gouvernorat= %s
        GROUP BY Sexe
        """
        df = pd.read_sql(query, con=engine, params=(selected_code,))
        plt.figure(figsize=(6,6))
        plt.pie(
        df['total_Population'],
        labels=df['Sexe'],
        autopct=lambda pct: autopct_format(pct, df['total_Population']),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe != "both" and not age:
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Gouvernorat = %s AND ID_Sexe = %s
        GROUP BY Sexe, ID_Sexe
    """
        df = pd.read_sql(query, con=engine, params=(selected_code, sexe))

        if df.empty:
            return "No data found for the selected delegation and sex.", 404

        plt.figure(figsize=(6, 6))
        plt.bar(df['Sexe'], df['total_Population'], color='skyblue')
        plt.xlabel('Sexe')
        plt.ylabel('Population')
        plt.title(f"Population for Sex: {df.iloc[0]['Sexe']} in Gouvernorat {df['total_Population'][0]}")
    
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe == "both" and age=="age":
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe, Classe_Age, Trancheage, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Gouvernorat= %s
        GROUP BY Sexe, ID_Sexe, Trancheage,Classe_Age
    """
        df = pd.read_sql(query, con=engine, params=(selected_code,))

        if df.empty:
            return "No data found for the selected delegation and sex.", 404

        df = pd.read_sql(query, con=engine, params=(selected_code,))
        print(df.columns)

        df = pd.read_sql(query, con=engine, params=(selected_code,))
        plt.figure(figsize=(20,20))
        df['label'] = df['Sexe'] + " (" + df['Trancheage'] + ")\n" + df['total_Population'].astype(str)
        plt.pie(

        df['total_Population'],
        labels=df['label'],
        autopct=lambda pct: autopct_format(pct,''),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe == "both" and age=="noage":
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Gouvernorat= %s
        GROUP BY Sexe, ID_Sexe, Trancheage
    """
        df = pd.read_sql(query, con=engine, params=(selected_code,))

        if df.empty:
            return "No data found for the selected delegation and sex.", 404

        df = pd.read_sql(query, con=engine, params=(selected_code,))
        print(df.columns)

        df = pd.read_sql(query, con=engine, params=(selected_code,))
        plt.figure(figsize=(20,20))
        df['label'] = df['Sexe'] +' ('+df['total_Population'].astype(str)+')'
        plt.pie(

        df['total_Population'],
        labels=df['label'],
        autopct=lambda pct: autopct_format(pct,''),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe != "both" and age=="age":
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe,Classe_Age, Trancheage, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Gouvernorat= %s AND ID_Sexe = %s
        GROUP BY Sexe, ID_Sexe, Trancheage,Classe_Age
    """
        df = pd.read_sql(query, con=engine, params=(selected_code,sexe))
        if df.empty:
            return "No data found for the selected delegation and sex.", 404


     
        plt.figure(figsize=(20,20))
        df['label'] = df['Sexe'] + " (" + df['Trancheage'] + ")\n" + df['total_Population'].astype(str)
        plt.pie(

        df['total_Population'],
        labels=df['label'],
        autopct=lambda pct: autopct_format(pct,''),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')
    elif sexe != "both" and age=="noage":
        if not selected_code:
            return "No Code_Gouvernorat provided", 400

        query = """
        SELECT Sexe, ID_Sexe, SUM(Population) AS total_Population
        FROM Population
        WHERE Code_Gouvernorat= %s AND ID_Sexe = %s
        GROUP BY Sexe, ID_Sexe, Trancheage
    """
        df = pd.read_sql(query, con=engine, params=(selected_code,sexe))
        if df.empty:
            return "No data found for the selected delegation and sex.", 404


     
        plt.figure(figsize=(20,20))
        df['label'] = df['Sexe'] +' ('+df['total_Population'].astype(str)+')'
        plt.pie(

        df['total_Population'],
        labels=df['label'],
        autopct=lambda pct: autopct_format(pct,''),
        startangle=140
        )
        plt.axis('equal')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')





if __name__ == "__main__":
    app.run(debug=True)

