from flask import Flask, render_template, request, redirect
#import pyodbc
import os
import pymysql

conn = pymysql.connect(
    host=os.environ["MYSQLHOST"],
    port=int(os.environ["MYSQLPORT"]),
    user=os.environ["MYSQLUSER"],
    password=os.environ["MYSQLPASSWORD"],
    database=os.environ["MYSQLDATABASE"],
    cursorclass=pymysql.cursors.DictCursor
)

# conn = pymysql.connect(
#     host="zephyr.proxy.rlwy.net",
#     port=26324,
#     user="root",
#     password="NdxajtflOEJCbxAqNEihvQhqodFOnJBw",
#     database="railway",
#     cursorclass=pymysql.cursors.DictCursor
# )


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/boeing")
def boeing():
    return render_template("boeing.html")

@app.route("/airbus")
def airbus():
    return render_template("airbus.html")

@app.route("/embraer")
def embraer():
    return render_template("embraer.html")

@app.route("/lotniska/europa")
def europa():
    return render_template("europa.html")

@app.route("/linie")
def linie():
    return render_template("linie.html")

@app.route("/db-test")
def db_test():
    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        result = cur.fetchone()
        return f"DB OK: {result}"



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