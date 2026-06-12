from flask import Flask, render_template, request, redirect, jsonify
#import pyodbc
import os
import pymysql


# conn = pymysql.connect(
#     host=os.environ["MYSQLHOST"],
#     port=int(os.environ["MYSQLPORT"]),
#     user=os.environ["MYSQLUSER"],
#     password=os.environ["MYSQLPASSWORD"],
#     database=os.environ["MYSQLDATABASE"],
#     cursorclass=pymysql.cursors.DictCursor
# )

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("MYSQLHOST", "zephyr.proxy.rlwy.net"),
        port=int(os.getenv("MYSQLPORT", 26324)),
        user=os.getenv("MYSQLUSER", "root"),
        password=os.getenv("MYSQLPASSWORD", "NdxajtflOEJCbxAqNEihvQhqodFOnJBw"),
        database=os.getenv("MYSQLDATABASE", "railway"),
        cursorclass=pymysql.cursors.DictCursor,
        charset="utf8mb4"
    )

@app.route('/flight/<int:flight_id>')
def flight(flight_id):

    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM v_flight_board
                WHERE id = %s
                ORDER BY data desc
            """, (flight_id,))

            flight = cursor.fetchone()

            # konwersja timedelta → string
            for k, v in flight.items():
                if hasattr(v, "total_seconds"):
                    flight[k] = str(v)

    finally:
        conn.close()

    return jsonify(flight)


@app.route('/')
def home():
    
    flights = []
    airlines = []

    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
          
               cursor.execute("""
                    SELECT *
                    FROM v_flight_board
                    WHERE data BETWEEN '2026-05-01' AND CURDATE()
                """)

        flights = cursor.fetchall()

    except Exception as e:
        print(f"Błąd SQL: {e}")

    finally:
        conn.close()

    return render_template(
        "index.html",
        flights=flights,
    )



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
     
    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, name
                FROM airline
                ORDER BY name
            """)

            airlines = cursor.fetchall()

    finally:
        conn.close()

    return render_template(
        "linie.html",
        airlines=airlines
    )



# @app.route("/db-test")
# def db_test():
#     with conn.cursor() as cur:
#         cur.execute("SELECT 1")
#         result = cur.fetchone()
#         return f"DB OK: {result}"



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