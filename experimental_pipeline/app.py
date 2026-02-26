# app.py
from fastapi import FastAPI
from main import run_experiment

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/run-experiment")
def run():
    run_experiment()
    return {"status": "Experiment executed and CSV saved"}
