from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Project": "He thong Quan ly Thu vien",
        "Student": "Nguyen Be Hiep",
        "ID": "DTC245200167",
        "Status": "Ung dung dang chay on dinh!"
    }
