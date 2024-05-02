from pydantic import BaseModel
class User(BaseModel):
    user_id: int
    name: str
    email: str
    password: str
    mobile: int


# this class is used for both User and Employer login purposes

class Login(BaseModel):
    email:str
    password:str

class Employer(BaseModel):
    emp_id: int
    job_id: int
    name: str
    email: str
    phone: int
    password: str

class JobPosting(BaseModel):
    job_id: int
    role: str
    company: str
    email: str
    emp_id: int
    
class JobApplication(BaseModel):
    job_id: int
    user_id: int
    resume: str
    skills: str

class Token(BaseModel):
    access_token: str
    token_type: str