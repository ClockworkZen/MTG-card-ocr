# Magic: The Gathering Card OCR Renamer

This Python tool uses EasyOCR and the Scryfall API to automatically rename image files of Magic: The Gathering cards based on the card name detected through OCR. Successfully identified cards are renamed and moved to a "Processed" folder, while unrecognized cards are moved to an "Error" folder.

Best used with Card Cropper!
[github](https://github.com/ClockworkZen/card-cropper)

## Prerequisites

Ensure you have the following installed before running the script:

1. **Python 3.x**: You can download Python from [python.org](https://www.python.org/downloads/).
2. **EasyOCR**: Install via pip.
3. **Requests Library**: Install via pip.

### Install Required Python Libraries

`pip install easyocr requests`

### Folder Structure
Ensure the following folder structure in the directory where you place the script:
```
/path_to_your_directory/
│
├── Import/
│   ├── image1.jpg
│   ├── image2.png
│   └── ... (other images)
│
├── Processed/ (created automatically)
│
├── Error/ (created automatically)
│
└── mtg_card_ocr_renamer.py (your script)
```
### Usage
Place Images: Place the images you want to process in the Import folder.
Run the Script: Execute the script using Python.

### Running the Script

`python mtg_card_ocr_renamer.py`

The script will process each image in the Import folder, rename the files based on the detected Magic: The Gathering card names, and move the files to the appropriate folders:

Processed: Contains successfully identified and renamed card images.
Error: Contains images where the card name could not be verified.

### Scryfall API
This tool uses the Scryfall API to verify the names of Magic: The Gathering cards detected through OCR. Scryfall provides a robust and comprehensive database of Magic: The Gathering cards, ensuring accurate verification and renaming of your card images.

### Contributions
Contributions are welcome! If you have any improvements or suggestions, please create a pull request or open an issue.

### License
This project is licensed under the MIT License.
