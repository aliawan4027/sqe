from fastapi import FastAPI
from fastapi.responses import FileResponse
from main import run_experiment
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API is running", "endpoints": ["/run-experiment", "/download-csv"]}

@app.post("/run-experiment")
def run():
    result = run_experiment()
    return {"status": "Experiment completed", "result": result}

@app.get("/download-csv")
def download():
    if os.path.exists("publishable_experiment_results.csv"):
        return FileResponse("publishable_experiment_results.csv", media_type="text/csv", filename="results.csv")
    return {"error": "CSV not found. Run /run-experiment first."}

