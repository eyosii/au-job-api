from fastapi import FastAPI
import requests
from requests.auth import HTTPBasicAuth

app = FastAPI()

SAP_API_URL = "https://hcm2preview.sapsf.eu/odata/v2/JobRequisition"

# Replace with your actual SAP SuccessFactors credentials
SAP_USERNAME = "TAMENEE@africanuniT1"
SAP_PASSWORD = "Eyosisjs123"

@app.get("/jobs")
def get_sap_jobs():
    try:
        response = requests.get(
            SAP_API_URL,
            auth=HTTPBasicAuth(SAP_USERNAME, SAP_PASSWORD),
            headers={
                "Accept": "application/json"
            }
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}
