from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Job(BaseModel):
    # id: int
    title: str
    company: str
    location: str
    salary: Optional[int] = 0
    remote: bool = False


# Define the API endpoints for jobs

@app.get("/")
def home():
    return {"message": "Welcome to the Job Portal API!"}

@app.get("/jobs")
def get_jobs():
    return[
        {"id": 1, "title": "Software Engineer", "company": "Tech Corp", "location": "New York", "salary": 10000, "remote": False},
        {"id": 2, "title": "Data Scientist", "company": "Data Inc.", "location": "San Francisco", "salary": 12000, "remote": True},
        {"id": 3, "title": "Instrumentation Tech", "company": "FLUXCORE", "location": "Kitwe", "salary": 8000, "remote": False}
    ]

@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    return {"id": job_id, 
            "title": "Software Engineer", 
            "company": "Tech Corp", 
            "location": "New York",
            "salary": 10000,
            "remote": False}


# Define the API endpoints for companies

@app.get("/companies")
def get_companies():
    return [
        {"id": 1, "name": "Tech Corp", "industry": "Technology"},
        {"id": 2, "name": "Data Inc.", "industry": "Data Analytics"},
        {"id": 3, "name": "FLUXCORE", "industry": "Instrumentation"}
    ]


# Define the API endpoints for workers

@app.get("/workers")
def get_workers():
    return [
        {"id": 1, "name": "Alice", "skills": ["Python", "Machine Learning"]},
        {"id": 2, "name": "Bob", "skills": ["JavaScript", "React"]},
        {"id": 3, "name": "Charlie", "skills": ["Instrumentation", "Data Analysis"]}
    ]


# Define the API endpoints for applications

@app.get("/applications")
def get_applications():
    return [
        {"id": 1, "worker_id": 1, "job_id": 1, "status": "Pending"},
        {"id": 2, "worker_id": 2, "job_id": 2, "status": "Accepted"},
        {"id": 3, "worker_id": 3, "job_id": 3, "status": "Rejected"}
    ]


@app.post("/jobs")
def create_job(job: Job):
    return {
        "message": "Job created successfully",
        "job": job
    }