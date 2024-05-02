import sqlite3
from fastapi import  FastAPI, HTTPException
from model.types import *
from Authentication import *
import uvicorn

app = FastAPI()

def verify_user(email:str, password:str):
    conn = sqlite3.connect("../revhire.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT email, password FROM User WHERE email=?", (email,))
    user = cursor.fetchone()
    
    conn.close()
    
    return (user[0] == email) and (user[1] == password)

def verify_employer(email:str, password:str):
    conn = sqlite3.connect("../revhire.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT email, password FROM EMPLOYEER WHERE email=?", (email,))
    employer = cursor.fetchone()
    conn.close()
    
    return (employer[0] == email) and (employer[1] == password)

def create_user(user: User):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO USER (user_id, name, email, password, mobile) VALUES (?, ?, ?, ?, ?)""", (user.user_id, user.name, user.email, user.password, user.mobile))

        conn.commit()
        conn.close()

        return {"message": "User created successfully"}
    except:
        raise HTTPException(status_code=500, detail="failed to create user")

def get_user(user_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM USER WHERE user_id = ?""", (user_id,))
        user = cursor.fetchone()

        conn.close()

        return {"user": user}
    except:
        return "No user found with that ID."

def update_user(user_id: int, user: User):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE USER SET name = ?, email = ?, password = ?, mobile = ? WHERE user_id = ?", 
                       (user.name, user.email, user.password, user.mobile, user_id))

        conn.commit()
        conn.close()

        return "User details updated successfully!"
    except:
        return "Error when updating the user details"

def delete_user(user_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM USER WHERE user_id = ?", (user_id,))

        conn.commit()
        conn.close()

        return "User deleted successfully!"
    except:
        return "Error when deleting the user."


"""This is for CRUD Operations for Employee Table"""


def create_employer(employer: Employer):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO EMPLOYEER (emp_id, job_id, name, email, phone, password) VALUES (?, ?, ?, ?, ?, ?)", (employer.emp_id, employer.job_id, employer.name, employer.email, employer.phone, employer.password))

        conn.commit()
        conn.close()

        return "Employeer created successfully"
    except:
        return HTTPException(status_code=500, detail="failed to create employer")

def get_employer(emp_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM EMPLOYEER WHERE emp_id = ?""", (emp_id,))
        employer = cursor.fetchone()

        conn.close()

        return employer
    except:
        return "Employer not found"

def update_employer(emp_id: int, employer: Employer):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE EMPLOYEER SET job_id = ?, name = ?, email = ?, phone = ?, password = ? WHERE emp_id = ?", (employer.job_id, employer.name, employer.email, employer.phone, employer.password, emp_id))

        conn.commit()
        conn.close()

        return "Employer details updated successfully!"
    except:
        return "Error when updating employer."

def delete_employer(emp_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM EMPLOYEER WHERE emp_id = ?", (emp_id,))

        conn.commit()
        conn.close()

        return "Employer deleted successfully!"
    except:
        return "Error when deleting the employer"


"""This is for CRUD Operations for JobPosting"""


def create_job_posting(job_posting: JobPosting):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO JOBPOSTING (job_id, role, company, email, emp_id) VALUES (?, ?, ?, ?, ?)", (job_posting.job_id, job_posting.role, job_posting.company, job_posting.email, job_posting.emp_id))

        conn.commit()
        conn.close()

        return "Job posting created successfully"
    except:
        return HTTPException(status_code=500, detail="failed to Create a Job Post")

def get_job_posting(job_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM JOBPOSTING WHERE job_id = ?", (job_id,))
        job_posting = cursor.fetchone()

        conn.close()

        return {"job_posting": job_posting}
    except:
        return "Error getting job posting details."

def update_job_posting(job_id: int, job_posting: JobPosting):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE JOBPOSTING SET role = ?, company = ?, email = ?, emp_id = ? WHERE job_id = ?", (job_posting.role, job_posting.company, job_posting.email, job_posting.emp_id, job_id))

        conn.commit()
        conn.close()

        return "Job posting updated successfully"
    except:
        return "Error updating job posting."

def delete_job_posting(job_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM JOBPOSTING WHERE job_id = ?", (job_id,))

        conn.commit()
        conn.close()

        return "Job posting deleted successfully"
    except:
        return "Error deleting job posting."


"""This is for CRUD Operations for JobApplication"""


def create_job_application(job_application: JobApplication):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO JOBAPPLICATION (job_id, user_id, resume, skills) VALUES (?, ?, ?, ?)", (job_application.job_id, job_application.user_id, job_application.resume, job_application.skills))

        conn.commit()
        conn.close()

        return "Job application Sent successfully!"
    except:
        return HTTPException(status_code=500, detail="failed to Apply a Job")


def get_job_application(job_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM JOBAPPLICATION WHERE job_id = ?", (job_id,))
        job_application = cursor.fetchone()

        conn.close()

        return job_application
    except:
        return  "No job applications found for that ID."

def update_job_application(job_id: int, job_application: JobApplication):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE JOBAPPLICATION SET user_id = ?, resume = ?, skills = ? WHERE job_id = ?", (job_application.user_id, job_application.resume, job_application.skills, job_id))

        conn.commit()
        conn.close()

        return "Job application updated successfully!"
    except:
        return "Error updating job application."

def delete_job_application(job_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM JOBAPPLICATION WHERE job_id = ?", (job_id,))

        conn.commit()
        conn.close()

        return "Job application deleted successfully"
    except:
        return "Error deleting job application."