'''
Jobless Monkeys: Aidan Wong, Abidur Rahman, Brian Liu, Leon Huang
SoftDev
P00: Move Slowly and Fix Things
2024-10-24
Time Spent: .05
'''

from flask import Flask, render_template, url_for
import os
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('landing.html')

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/register")
def register_page():
    return render_template('register.html')

@app.route("/dashboard")
def dashboard_page():
    return "Dashboard goes here"

@app.route("/create")
def create_page():
    return "Story Creator goes here"

@app.route("/view")
def view_page():
    return "Story viewer goes here"

@app.route("/collection")
def collection_page():
    return "Story Collection goes here"

@app.route("/contribute")
def contribute_page():
    return "Story Contribution goes here"

if __name__ == "__main__":
    app.debug = True
    app.run()