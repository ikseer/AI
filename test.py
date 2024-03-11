from fastapi.testclient import TestClient
from main import app
import os
client = TestClient(app)

def test_upload_image():
    # Read a sample image file in binary mode
    image_path="Ai_model/Inputs/img.JPG"
    assert os.path.exists(image_path)
    with open(  image_path,"rb") as image_file:
        files = {"image": ("test_image.jpg", image_file, "image/jpeg")}
        response = client.post("/upload/", files=files)
    
    assert response.status_code == 200
    assert "result" in response.json()
    print(response.json())

if __name__ == "__main__":
    test_upload_image()
