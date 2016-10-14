import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...


# students TABLE
q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(q)    #run SQL query

fObj = open("peeps.csv") 
d1=csv.DictReader(fObj)

for k in d1:
    params = (k['name'], k['age'], k['id'])
    c.execute("INSERT INTO students VALUES (?,?,?)", params)
fObj.close()



# courses TABLE
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)

fObj = open("courses.csv")
d2=csv.DictReader(fObj)

for k in d2:
    params = (k['code'], k['mark'], k['id'])
    c.execute("INSERT INTO courses VALUES (?,?,?)", params)
fObj.close()

#==========================================================
db.commit() #save changes
db.close()  #close database


