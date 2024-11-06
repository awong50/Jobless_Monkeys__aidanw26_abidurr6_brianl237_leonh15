import sqlite3   #enable control of an sqlite database     

DB_FILE="discobandit.db"

def initDB():
    db = sqlite3.connect(DB_FILE) # Open/Create database file
    c = db.cursor()
    
    c.execute("""
              CREATE TABLE users (
              username TEXT, 
              password TEXT
              )
              """) # creates login database
    c.execute("""
              CREATE TABLE collection (
              id INTEGER, 
              title TEXT, 
              contentR TEXT, 
              versionC INTEGER, 
              authorL TEXT,
              PRIMARY KEY(id, title)
              )
              """) # creates story database
    c.execute("""
              CREATE TABLE story (
              id INTEGER, 
              version INTEGER, 
              vcontent TEXT, 
              vauthor TEXT,
              FOREIGN KEY (id) REFERENCES collection (id)
              )
              """) # creates story database
    
    db.commit() #save changes
    db.close()  #close database

def addUser(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    query = "INSERT INTO users (username, password) VALUES (?, ?)"
    c.execute(query, (username, password))
    db.commit()
    db.close()

def checkUser(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username, )) # Passing username as a single element tuple
    user = c.fetchone() # Checks to see if any rows were returned
    if user is not None:
        if password == user[1]:
            return True
    return False

def registerUser(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username, )) # Passing username as a single element tuple
    user = c.fetchone() # Checks to see if any rows were returned
    if user is None:
        addUser(username, password)
        return True
    return False


def addVersion(id, version, vcontent, vauthor):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    query = "INSERT INTO story (id, version, vcontent, vauthor) VALUES (?, ?, ?, ?)"
    c.execute(query, (id, version, vcontent, vauthor))
    db.commit()
    db.close()

def createStory(title, contentR, authorL):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT MAX(id) FROM collection")
    latest_id = c.fetchone()[0] # Grabs the first row, None if no rows exist

    new_id = 1 if latest_id is None else latest_id + 1

    c.execute("INSERT INTO collection (id, titles, contentR, versionC, authorL) VALUES (?, ?, ?, ?, ?)", (new_id, title, contentR, 0, authorL))
    db.commit()
    db.close()

    addVersion(new_id, 0, contentR, authorL) # Adds the version to the individual story
    
def contributionList(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT id FROM story WHERE vauthor=?", (username, ))
    stories = c.fetchall()

    if not stories:
        db.close()
        return []

    c.execute("SELECT titles, versionC, authorL, id FROM collection WHERE id IN (SELECT id FROM story WHERE vauthor=?)", (username, ))

    titles = c.fetchall()
    db.close()
    # print(titles)
    return titles 

def displayStory(id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT vcontent FROM story WHERE id=?", (id, ))
    stories = c.fetchall()

    db.close()

    return stories

def displayStoryTitle(id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT titles FROM collection WHERE id=?", (id, ))
    title = c.fetchone()

    db.close()

    return title[0]

def checkContributionStatus(username, story_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT id FROM story WHERE vauthor=? AND id=?", (username, story_id))

    ids = c.fetchone()

    db.close()

    return ids is not None

def displayCollection():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT titles, versionC, authorL, id FROM collection")

    stories = c.fetchall()

    db.close()

    if not stories:
        return []
    
    return stories

def displayLastVersion(id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT vcontent, vauthor FROM story WHERE id=?", (id, ))

    stories = c.fetchall()

    db.close()

    if not stories:
        db.close()
        return []
    
    return stories[0]