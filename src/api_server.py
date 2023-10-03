from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model import infer
from PIL import Image
import io
from io import BytesIO


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/clip_inference')
async def clip_inference(file: UploadFile = File(...), text_input: str = Form(None)):

    if not file:
        print("image file not found!")
        return str("image file not found!")
    if not text_input:
        print("input text not found!")
        return str("text not found!")
        
    image_byte = await file.read()
    img = Image.open(io.BytesIO(image_byte))
    output_pred = infer(text_input, img)

    return output_pred

