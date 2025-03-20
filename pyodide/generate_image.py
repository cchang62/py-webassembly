import base64
from PIL import Image, ImageDraw
from io import BytesIO
import json

def generate_image(json_data):
    # Parse JSON data
    data = json.loads(json_data)
    text = data["text"]
    font_size = data["fontSize"]
    width = data["width"]
    height = data["height"]

    # Create an image
    image = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill="black")  # Simple text rendering

    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str
