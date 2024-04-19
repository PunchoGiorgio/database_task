import sqlite3 as sq

con = None
try:
    con = sq.connect("performance.db")
    cur = con.cursor()

    cur.executescript(
        """CREATE TABLE IF NOT EXISTS performance (
        stud_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        surname TEXT, 
        subject TEXT,                        
        mark INTEGER);
        
        BEGIN;  
                
        INSERT INTO performance VALUES(NULL, 'John', 'Smith', 'Physics', 5);  
        INSERT INTO performance VALUES(NULL, 'Sean', 'Martin', 'Chemistry', 4);
        INSERT INTO performance VALUES(NULL, 'Pamela', 'Presley', 'Algebra', 5);
        INSERT INTO performance VALUES(NULL, 'Sam', 'Brody', 'Biology', 3);
        INSERT INTO performance VALUES(NULL, 'Stephanie', 'Connors', 'Geometry', 5);
    """
    )

    con.commit()

except sq.Error:
    if con:
        con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con:
        con.close()

con = None
try:
    con = sq.connect("library.db")
    cur = con.cursor()
    cur.executescript(
        """CREATE TABLE IF NOT EXISTS library (
        subscript_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        surname TEXT, 
        book TEXT,                        
        receive_date DATE,
        actual_return DATE,
        planned_term INTEGER);
        
        BEGIN;  
                
        INSERT INTO library VALUES(NULL, 'Sam', 'Elliot', 'War & Peace', '2017-05-22', '2017-06-22', 10);  
        INSERT INTO library VALUES(NULL, 'Mike', 'Myers', 'The Catcher in the Rye', '2010-07-16', '2010-07-25', 10);
        INSERT INTO library VALUES(NULL, 'Melissa', 'Shepard', 'Mass Effect', '2021-09-17', '2021-11-07', 10);
        INSERT INTO library VALUES(NULL, 'Patricia', 'Connors', 'Shining', '2010-07-16', '2010-07-20', 10);
        INSERT INTO library VALUES(NULL, 'Bruce', 'Abbot', 'Spy', '2010-09-04', '2010-10-20', 10);
        INSERT INTO library VALUES(NULL, 'Mark', 'Hansen', 'Spy', '2022-03-01', '2022-03-09', 10);
        INSERT INTO library VALUES(NULL, 'Sam', 'Waters', 'Mass Effect', '2020-04-11', '2020-11-11', 10);
        INSERT INTO library VALUES(NULL, 'Samantha', 'Shepard', 'Mass Effect', '2023-10-14', '2023-10-18', 10);                                          
    """
    )

    con.commit()

except sq.Error:
    if con:
        con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con:
        con.close()
