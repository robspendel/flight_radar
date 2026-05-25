from flask import Flask, render_template, request, redirect
#import pyodbc
app = Flask(__name__)

@app.route('/')
def b738():
    return render_template("index.html")

@app.route("/airbus")
def airbus():
    return render_template("airbus.html")

@app.route("/embraer")
def embraer():
    return render_template("embraer.html")
# ----------------------------------------------------
# KONFIGURACJA POŁĄCZENIA
# ----------------------------------------------------
# conn_str = (
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=RAKS-ASUS_EB\\SQLEXPRESS;"
#     "DATABASE=ksiegarnia1;"
#     "UID=sa;"
#     "PWD=110360poznan;"
# )

# def get_connection():
#     return pyodbc.connect(conn_str)

# # ----------------------------------------------------
# # STRONA GŁÓWNA
# # ----------------------------------------------------
# @app.route("/", methods=["GET", "POST"])
# def index():
#     conn = get_connection()
#     cursor = conn.cursor()