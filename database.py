import sqlite3

con = sqlite3.connect("revhire.db")

cursor = con.cursor()

# User's Table

cursor.execute(
   """CREATE TABLE USER(
       user_id INTEGER PRIMARY KEY,
       name VARCHAR(20),
       email VARCHAR(20) UNIQUE,
       password VARCHAR(20) UNIQUE,
       Mobile INTEGER UNIQUE
   )""")

# Employer Table

cursor.execute(
    """
    CREATE TABLE EMPLOYEER(
        emp_id INTEGER(15) PRIMARY KEY,
        job_id INTEGER(15) REFERENCES JOBAPPLICATION(job_id),
        emp_name VARCHAR(25), 
        email VARCHAR UNIQUE,
        contact_number INTEGER UNIQUE, 
        Password VARCHAR(8) UNIQUE
    )""")

# JobPosting Table

cursor.execute(
    """
    CREATE TABLE JOBPOSTING(
        job_id INTEGER(10) PRIMARY KEY, 
        role VARCHAR NOT NULL,
        company VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE,
        emp_id INTEGER(10) NOT NULL REFERENCES EMPLOYEER(emp_id)
    )""")

# JobAplication Table

cursor.execute(
    """
    CREATE TABLE JOBAPPLICATION(
        job_id INTEGER(10) PRIMARY KEY, 
        user_id INTEGER(10) REFERENCES USER(user_id),
        resume VARCHAR(50) NOT NULL UNIQUE,
        skills VARCHAR(400) NOT NULL
    )""")

con.commit()

con.close()