import os
import easyocr
from PIL import Image
import cv2
import shutil
import requests
import re

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    try:
        # Use EasyOCR to extract text
        results = reader.readtext(image_path)

        # Extract the card name (assuming it's the first line of the text)
        if results:
            card_name = results[0][1].strip()
            return card_name, results
        else:
            return None, "No text detected"
    except Exception as e:
        return None, str(e)

def get_verified_card_name(card_name):
    try:
        response = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={card_name}")
        if response.status_code == 200:
            data = response.json()
            return data['name']  # Get the exact card name from the database
        else:
            return None
    except Exception as e:
        return None

def sanitize_filename(name):
    # Remove any invalid characters for Windows file names
    return re.sub(r'[\\/*?:"<>|]', "", name)

def ensure_directories_exist():
    if not os.path.exists('Processed'):
        os.makedirs('Processed')
    if not os.path.exists('Error'):
        os.makedirs('Error')

def rename_images_in_folder():
    import_folder = 'Import'
    processed_folder = 'Processed'
    error_folder = 'Error'

    ensure_directories_exist()

    for filename in os.listdir(import_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(import_folder, filename)
            print(f"Processing file: {filename}")
            card_name, ocr_result = extract_text_from_image(image_path)

            if card_name:
                verified_card_name = get_verified_card_name(card_name)
                if verified_card_name:
                    sanitized_card_name = sanitize_filename(verified_card_name)
                    new_filename = f"{sanitized_card_name}.jpg"
                    new_path = os.path.join(processed_folder, new_filename)

                    # Check for naming conflicts and resolve by appending a number
                    if os.path.exists(new_path):
                        base, extension = os.path.splitext(new_filename)
                        counter = 1
                        while os.path.exists(new_path):
                            new_filename = f"{base}_{counter}{extension}"
                            new_path = os.path.join(processed_folder, new_filename)
                            counter += 1

                    shutil.move(image_path, new_path)
                    print(f"Renamed and moved '{filename}' to '{new_filename}' in 'Processed'")
                else:
                    error_path = os.path.join(error_folder, filename)
                    shutil.move(image_path, error_path)
                    print(f"Moved '{filename}' to 'Error'. Unable to verify card name: '{card_name}'")
            else:
                error_path = os.path.join(error_folder, filename)
                shutil.move(image_path, error_path)
                print(f"Moved '{filename}' to 'Error'. OCR failed with error: '{ocr_result}'")

    input("Processing complete. Press Enter to exit...")

# Rename the images in the 'Import' folder
rename_images_in_folder()
