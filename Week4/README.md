# Week4 Assessment

## Quiz: Many-to-Many Relationships and Python
1. How do we model a many-to-many relationship between two database tables?
    A. We add a table with two foreign keys
    
2. In Python, what is a database 'cursor' most like?
    A. A file handle

3. What method do you call in an SQLite cursor object in Python to run an SQL command?
    A. execute()
    
4. In the following SQL,What does the LIMIT clause in the following SQL accomplish?
~~~sql
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))')
~~~
what is the purpose of the "?"?
    A. It is a placeholder for the contents of the "org" variable
    
5. In the following Python code sequence (assuming cur is a SQLite cursor object),
~~~sql
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
row = cur.fetchone()
~~~
what is the value in row if no rows match the WHERE clause?
    A. None
    
6. What does the LIMIT clause in the following SQL accomplish?
~~~sql
SELECT org, count FROM Counts 
   ORDER BY count DESC LIMIT 10
~~~
A. It only retrieves the first 10 rows from the table

7. What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do?
    A. It allows multiple SQL statements separated by semicolons
    
8. What is the purpose of "OR IGNORE" in the followin SQL:
~~~sql
INSERT OR IGNORE INTO Course (title) VALUES ( ? )
~~~ 
A. It makes sure that if a particular title is already in the table, there are no duplicate rows inserted. 

9. What do we generally avoid in a many-to-many junction table? (not answer)
    A. Data items specific to the many-to-many relationship

## Week4 Many students in Many Courses
### Instructions
This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - this code is incomplete as you need to modify the program to store the role column in the Member table to complete the assignment.

Each student gets their own file for the assignment. Download this file and save it as roster_data.json. Move the downloaded file into the same folder as your roster.py program.

Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, run the following SQL command:
~~~sql
SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
~~~
Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.
