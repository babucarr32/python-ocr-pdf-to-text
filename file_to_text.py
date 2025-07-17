import sys
import os
from pathlib import Path
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_image(image_path: Path) -> str:
    return pytesseract.image_to_string(Image.open(image_path))

def extract_text_from_pdf(pdf_path: Path) -> str:
    images = convert_from_path(str(pdf_path))
    text = ""
    for i, image in enumerate(images):
        print(f"Page {i}")
        text += pytesseract.image_to_string(image) + "\n"
    return text

def main(input_path_str):
    input_path = Path(input_path_str)
    if not input_path.exists():
        print(f"Error: {input_path} does not exist.")
        return

    if input_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        text = extract_text_from_image(input_path)
    elif input_path.suffix.lower() == ".pdf":
        text = extract_text_from_pdf(input_path)
    else:
        print("Unsupported file format. Please provide a PDF or image file.")
        return

    output_path = input_path.with_suffix('.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Text extracted and saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_text.py <path_to_pdf_or_image>")
    else:
        main(sys.argv[1])

