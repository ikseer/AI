from fastapi.responses import JSONResponse
from read_perception.Text_extraction import text_extraction
from fastapi import FastAPI, File, UploadFile, Request


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Adjust if needed


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
from PIL import Image

@app.get("/", response_class=HTMLResponse)
async def upload_image_form( request: Request):
    """
    Displays the HTML form to upload an image.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def receive_name_and_image(image: UploadFile = File(...)):
    """
    Receives an image from a POST request.

    Args:
        image (UploadFile): The uploaded image file.

    Returns:
        JSONResponse: A JSON response containing a text result.
    """
    image_path=f"{image.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)


    text = text_extraction(image_path)  # Pass the byte array to text_extraction
    # remove the image
    os.remove(image_path)
    return JSONResponse(content=text)
    # return JSONResponse(content={"result": text})

  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
