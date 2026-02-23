from fastapi import FastAPI
from tools import search_clothing_stores
from utils import estimate_footfall
from agent import generate_report
from report_generator import create_pdf

app = FastAPI()

@app.get("/competitor-analysis")
def competitor_analysis(location: str):
    stores = search_clothing_stores(location)
    
    for store in stores:
        store["footfall"] = estimate_footfall(store["reviews"])
    
    report = generate_report(location, stores)
    
    pdf_file = create_pdf(report)
    
    return {
        "stores": stores,
        "report": report,
        "pdf": pdf_file
    }