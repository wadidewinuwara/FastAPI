from fastapi import FastAPI, UploadFile
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

DATA = Path() / 'DATA'

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file_upload: UploadFile):
    data = await file_upload.read()
    save_to = DATA / file_upload.filename
    with open(save_to, 'wb') as f:
        f.write(data)

    return {"filename": save_to}
