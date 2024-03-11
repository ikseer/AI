from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
from Ai_model.Text_extraction import text_extraction
app = FastAPI()

from PIL import Image



@app.post("/upload")
async def receive_name_and_image(image: UploadFile = File(...)):
    """
    Receives an image from a POST request.

    Args:
        image (UploadFile): The uploaded image file.

    Returns:
        JSONResponse: A JSON response containing a text result.
    """
    image_path=f"data/{image.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)


    text = text_extraction(image_path)  # Pass the byte array to text_extraction
    # remove the image
    os.remove(image_path)
    return JSONResponse(content={"result": text})

  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
