from app import app
from flask import render_template, redirect, url_for, flash, request
#from app import db

@app.route("/")
def home_page():
    return render_template("index.html")


