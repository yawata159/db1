import sqlite3

f="discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()    
d = db.cursor()

# look up the grades for each student
def getGrades(student):
    query = "SELECT mark FROM courses, students WHERE courses.id = students.id and name = ?"
    c.execute(query, (student,))
    return [elem[0] for elem in c];

# compute the average for each student
def getAverage(student):
    grades = getGrades(student);
    total = 0;
    for grade in grades:
        total+=grade

    return total/float(len(grades))

# display each student's name, id and average
def printAverages():
    query = "SELECT name, id FROM students"
    d.execute(query)
    for value in d:
        print "Name: %s , Id: %d , Average: %f" %(value[0],value[1],getAverage(value[0]))

printAverages()
