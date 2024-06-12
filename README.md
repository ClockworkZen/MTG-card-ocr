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
├── Error/ (created automatically)I didn
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

### Enabling CUDA

This has only been tested on Windows.

 1. Download and install [CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
 2. Downlaod and install [cuDNN](https://developer.nvidia.com/cudnn-downloads)
  3. Set your PATH directories correctly with the following commands
     ```
     setx PATH "%PATH%;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp;C:\tools\cuda\bin"
     setx CUDA_HOME "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8"
     
  4. Verify that your paths are correct by using the following command on the command line:
     `nvcc --version`
 5. Install the correct version of Torch using the following command:
`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`

If everything is set up correctly, open up a python console and execute the following command: 
```
import torch
print(torch.cuda.is_available())
```
If this returns True, you can use CUDA now!


### Contributions
Contributions are welcome! If you have any improvements or suggestions, please create a pull request or open an issue.

### License
This project is licensed under the MIT License.
