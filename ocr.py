import pytesseract
from PIL import Image


def extract_text_from_image(image):
    """
    Extract text from an uploaded image using Tesseract OCR.
    """

    text = pytesseract.image_to_string(image)

    return text.strip()