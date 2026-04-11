from fastapi import FastAPI,Path
import json
app = FastAPI() 

def load_data():
    # Simulate loading data from a file or database
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data


@app.get("/")
def hello():
    return {"message": "Patients Management System"}

@app.get("/about")
def about():
    return {"message": "About Us"}
@app.get("/view")
def view():
    data = load_data()  
    return data
@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve",example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id] 
    return {"message": "Patient not found"}