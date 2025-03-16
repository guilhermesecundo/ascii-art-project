import sys
import os
import tkinter as tk
from PIL import Image
from tkinter import filedialog

# Adiciona o diretório 'src/' ao caminho do Python
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from image_processor import process_image
from ascii_converter import ASCIIConverter

# Integração entre image_processor e ascii_converter
def select_image():
    root = tk.Tk()
    root.withdraw()
    file_image = filedialog.askopenfilename(
        title="Image select",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")],
    )
    return file_image

def main():
    input_image = select_image()

        
    if input_image == "":
        print("No image selected or invalid image.")
    
    else: 
        try:
            Image.open(input_image).verify()
        except Exception:
            print("Error: Invalid image or corrupted image.")
            return
        
        else:
            processed_image = "processed_output.jpg"  
            ascii_output = "output_ascii.txt" 

        print("Processing the image...")
        process_image(input_image, processed_image, max_width=20)  

        print("Converting the processed image into ASCII art...")
        converter = ASCIIConverter()
        ascii_art = converter.image_to_ascii(processed_image)  

        print("Saving the ASCII art...")
        converter.save_ascii_art(ascii_art, ascii_output)

        print(f"Test completed! ASCII art saved in {ascii_output}")   
    

        print("Processing the image...")
        process_image(input_image, processed_image, max_width=350)  

        print("Converting the processed image intoASCII art...")
        converter = ASCIIConverter()
        ascii_art = converter.image_to_ascii(processed_image)  

        print("Saving the ASCII art...")
        converter.save_ascii_art(ascii_art, ascii_output)


if __name__ == "__main__":
    main()
    
#funcinando