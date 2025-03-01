from fastapi import FastAPI
from pydantic import BaseModel
from matcher import match_resume_to_jobs

app = FastAPI()

# Example job descriptions dataset
job_data = {
    "Software Engineer": "Develop software applications using Python and JavaScript.",
    "Data Scientist": "Analyze data using machine learning and deep learning.",
    "AI Engineer": "Build AI models using TensorFlow and PyTorch.",
}

class ResumeInput(BaseModel):
    resume_text: str

@app.post("/match-jobs")
async def match_jobs(input_data: ResumeInput):
    matches = match_resume_to_jobs(input_data.resume_text, job_data)
    return {"matches": matches}
