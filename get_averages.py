import sqlite3

f="discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()    

# look up the grades for each student
def getGrades(student):
    query = "SELECT mark FROM courses, students WHERE courses.id = students.id and name = ?"
    c.execute(query, (student,) )
    return [elem[0] for elem in c.fetchall()];

print getGrades("kruder")

# compute the average for each student
def getAverage(student):
    grades = getGrades(student);
    total = 0;
    numGrades = 0;
    for grade in grades:
        total+=grade
        numGrades+=1

    return total/numGrades

print getAverage("kruder")
