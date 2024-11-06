import sqlite3   #enable control of an sqlite database     

DB_FILE="discobandit.db"

def initDB():
    db = sqlite3.connect(DB_FILE) # Open/Create database file
    c = db.cursor()
    
    c.execute("""
              CREATE TABLE IF NOT EXISTS users (
              username TEXT, 
              password TEXT
              )
              """) # creates login database
    c.execute("""
              CREATE TABLE IF NOT EXISTS collection (
              id INTEGER, 
              title TEXT, 
              contentR TEXT, 
              versionC INTEGER, 
              authorL TEXT,
              PRIMARY KEY(id, title)
              )
              """) # creates story database
    c.execute("""
              CREATE TABLE IF NOT EXISTS story (
              id INTEGER, 
              version INTEGER, 
              vcontent TEXT, 
              vauthor TEXT,
              FOREIGN KEY (id) REFERENCES collection (id)
              )
              """) # creates story database
    
    db.commit() #save changes
    db.close()  #close database

############################# User Database Interations #############################
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


############################# Story Database Interactions #############################

# Adds version to story table
def addVersion(id, version, vcontent, vauthor):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    query = "INSERT INTO story (id, version, vcontent, vauthor) VALUES (?, ?, ?, ?)"
    c.execute(query, (id, version, vcontent, vauthor))
    db.commit()
    db.close()

# Creates a new story
def createStory(title, contentR, authorL):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT MAX(id) FROM collection")
    latest_id = c.fetchone()[0] # Grabs the first row, None if no rows exist

    new_id = 1 if latest_id is None else latest_id + 1

    c.execute("INSERT INTO collection (id, title, contentR, versionC, authorL) VALUES (?, ?, ?, ?, ?)", (new_id, title, contentR, 0, authorL))
    db.commit()
    db.close()

    addVersion(new_id, 0, contentR, authorL) # Adds the version to the individual story

# Contribute to an existing story
def contributeStory(story_id, addition, author):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT MAX(version) FROM story WHERE id=?", (story_id, ))

    latest_version = c.fetchone()[0]
    new_version = 1 if latest_version is None else latest_version + 1

    c.execute("UPDATE collection SET contentR=?, versionC=? WHERE id=?", (addition, new_version, story_id))

    db.close()

    addVersion(story_id, new_version, addition, author)

############################# Display Functions #############################

# Dashboard function - Displays list of stories that user has contributed to
def contributionList(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT id FROM story WHERE vauthor=?", (username, ))
    stories = c.fetchall()

    if not stories:
        db.close()
        return []

    c.execute("SELECT title, versionC, authorL, id FROM collection WHERE id IN (SELECT id FROM story WHERE vauthor=?)", (username, ))

    titles = c.fetchall()
    db.close()
    # print(titles)
    return titles 

# Function that returns list of versions of a specific story
def displayStory(id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT vcontent, vauthor FROM story WHERE id=?", (id, ))
    stories = c.fetchall()

    db.close()

    return stories

# Function that returns title of a specific story id
def displayStoryTitle(id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT title FROM collection WHERE id=?", (id, ))
    title = c.fetchone()

    db.close()

    return title[0]

# Function that checks if a user has contributed to a story (to determine their view status)
def checkContributionStatus(username, story_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT id FROM story WHERE vauthor=? AND id=?", (username, story_id))

    ids = c.fetchone()

    db.close()

    return ids is not None

# Function for the collections page - Grab information to display
def displayCollection():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT title, versionC, authorL, id FROM collection")

    stories = c.fetchall()

    db.close()

    if not stories:
        return []
    
    return stories

# Function that shows the latest version for users that have not contributed to a page
def displayLastVersion(id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT vcontent, vauthor FROM story WHERE id=? ORDER BY version DESC LIMIT 1", (id, ))

    stories = c.fetchall()

    db.close()

    if not stories:
        db.close()
        return []
    
    print(stories[0])
    
    return stories[0]

