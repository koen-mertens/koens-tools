import os
import pytesseract

from PIL import Image

# Specify the path to your directory
directory_path = '***'
pytesseract.pytesseract.tesseract_cmd = r'***/tesseract.exe'
file_path = '***/output.txt'
file_path2 = '***/outputWithMarks.txt'
# Loop through files in the directory
for entry in os.listdir(directory_path):
    # Construct the full path to the file or directory
    full_path = os.path.join(directory_path, entry)
    
    # Check if it's a file
    if os.path.isfile(full_path):  
        img = Image.open(full_path)
        text = pytesseract.image_to_string(img)
        with open(file_path, 'a') as file:
            file.write(text)
        markedText = "---"+entry+"---"+text+"---"+entry+"---"
        with open(file_path2, 'a') as file:
            file.write(markedText)
