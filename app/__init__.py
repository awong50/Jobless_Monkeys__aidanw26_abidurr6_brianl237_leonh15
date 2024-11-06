'''
Jobless Monkeys: Aidan Wong, Abidur Rahman, Brian Liu, Leon Huang
SoftDev
P00: Move Slowly and Fix Things
2024-10-24
Time Spent: .05
'''

from flask import Flask, render_template, url_for, session, request, redirect
from DBModules import dbFunctions
import os


app = Flask(__name__)

app.secret_key = os.urandom(32)

dbFunctions.initDB()

@app.route("/", methods=['GET', 'POST'])
def landing_page():
    form_type = request.form.get('form_type')
    if form_type == 'login':
        return redirect(url_for('login_page'))
    if form_type == 'register':
        return redirect(url_for('register_page'))
    return render_template('landing.html')

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form_type = request.form.get('form_type')
    if form_type == 'sign_in':
        name = request.form.get('name')
        password = request.form.get('password')
        if dbFunctions.checkUser(name, password):
            session['username'] = name
            return redirect(url_for('dashboard_page'))
        else:
            return render_template('login.html', errorL = "USERNAME OR PASSWORD IS INCORRECT")
    if form_type == 'toLanding':
        return redirect(url_for('landing_page'))
    return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form_type = request.form.get('form_type')
    if form_type == 'sign_up':
        name = request.form.get('name')
        password = request.form.get('password')

        if dbFunctions.registerUser(name, password):
            session['username'] = name
            return redirect(url_for('dashboard_page'))
        else:
            return render_template('register.html', errorS="USERNAME TAKEN")
    if form_type == 'toLanding':
        return redirect(url_for('landing_page'))
    return render_template('register.html')

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard_page():
    if 'username' in session:
        returnName = session['username']
        form_type = request.form.get('form_type')

        if form_type == 'log_out':
            session.pop('username')
            return redirect(url_for('landing_page'))
        
        if form_type == 'create':
            return redirect(url_for('create_page'))
        
        if form_type == 'toCollection':
            return redirect(url_for('collection_page'))
        
        if form_type is not None and form_type[0: 4] == 'view':
            return redirect(url_for('view_page', story_id = form_type[4:])) 
        
        storiesToAdd = dbFunctions.contributionList(returnName)

        return render_template('dashboard.html', username=returnName, stories=storiesToAdd)
    
    return redirect(url_for('landing_page'))

@app.route("/create", methods=['GET', 'POST'])
def create_page():
    if 'username' in session:
        form_type = request.form.get('form_type')
        if form_type == 'log_out':
            session.pop('username')
            return redirect(url_for('landing_page'))
        if form_type == 'create':
            title = request.form.get('title')
            content = request.form.get('story')
            author = session['username']
            dbFunctions.createStory(title, content, author)
            return redirect(url_for('dashboard_page'))
        if form_type == 'toDashboard':
            return redirect(url_for('dashboard_page'))
        return render_template('create.html')
    return redirect(url_for('landing_page'))
        

@app.route("/view/<story_id>", methods=['GET', 'POST']) # Add <story_id> to generate specific pages
def view_page(story_id):
    if 'username' in session:
        username = session['username']
        form_type = request.form.get('form_type')
        story = dbFunctions.displayStory(story_id)
        title = dbFunctions.displayStoryTitle(story_id)
        isContributer = dbFunctions.checkContributionStatus(username, story_id)
        latestVersion = dbFunctions.displayLastVersion(story_id)
        if form_type == 'contribute':
            return redirect(url_for('contribute_page', story_id=story_id))
        if form_type == 'toDashboard':
            return redirect(url_for('dashboard_page'))
        if form_type == 'toCollection':
            return redirect(url_for('collection_page'))
        return render_template('view.html', title=title, story=story, currentContributer=isContributer, latestVersion=latestVersion[0], author=latestVersion[1])
    return redirect(url_for('landing_page'))

@app.route("/collection", methods=['GET', 'POST'])
def collection_page():
    if 'username' in session:
        form_type = request.form.get('form_type')
        collection = dbFunctions.displayCollection()
        if form_type is not None and form_type[0: 4] == 'view':
            return redirect(url_for('view_page', story_id = form_type[4:])) 
        if form_type == 'toDashboard':
            return redirect(url_for('dashboard_page'))
        return render_template('collection.html', stories=collection)
    return redirect(url_for('landing_page'))
    

@app.route("/contribute/<story_id>", methods=['GET', 'POST'])
def contribute_page(story_id):
    if 'username' in session:

        form_type = request.form.get('form_type')
        title = dbFunctions.displayStoryTitle(story_id)
        lastAuthor = dbFunctions.displayLastVersion(story_id)[1]
        latestContent = dbFunctions.displayLastVersion(story_id)[0]

        if form_type == 'log_out':
            session.pop('username')
            return redirect(url_for('landing_page'))
        
        if form_type == 'contribute':
            content = request.form.get('story')
            author = session['username']
            dbFunctions.contributeStory(story_id, content, author)
            return redirect(url_for('dashboard_page'))
        
        if form_type == 'toDashboard':
            return redirect(url_for('dashboard_page'))
        
        return render_template('contribute.html', title=title, lastAuthor=lastAuthor, latestContent=latestContent)
    
    return redirect(url_for('landing_page'))

if __name__ == "__main__":
    app.debug = True
    app.run()