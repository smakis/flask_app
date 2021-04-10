from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=False)
app.config.from_pyfile("config.py")
key = app.config["SECRET_KEY"]
db = app.config["SQLALCHEMY_DATABASE_URI"]


@app.route("/")
def home():
    return render_template("main.html", name=session.get("username", "unknown"))
