from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME")
        )
        return " Flask connected to MySQL successfully!"
    except Exception as e:
        return f" Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
