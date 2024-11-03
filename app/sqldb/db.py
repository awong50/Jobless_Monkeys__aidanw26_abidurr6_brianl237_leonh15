import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

#tentative file for db work
c.execute("CREATE TABLE login (username TEXT, password TEXT)") #creates login database
c.execute("CREATE TABLE stories (id int, titles TEXT, content TEXT, version int)") #creates story database
c.execute("CREATE TABLE story (id int, latestauthor TEXT, latestcontent TEXT, version int)") #creates story database
c.execute("CREATE TABLE authors (username TEXT, perm TEXT, version int)") #creates author table database


#==========================================================

db.commit() #save changes
db.close()  #close database

